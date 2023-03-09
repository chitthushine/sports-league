from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from .forms import MatchForm
from .models import Match
from .utils import get_rankings

class MatchTestCase(TestCase):
    def setUp(self):
        """
        Setup for login user and one match data.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', 
                                             password='testpass')
        self.match = Match.objects.create(team_1='Team A', team_2='Team B',\
                                          team_1_score=2, team_2_score=1)

    def test_match_new_view(self):
        """
        Test that match_new view can be accessed only by authenticated 
        user and new match can be created.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('match_new'), 
                                    {'team_1': 'Team C', 'team_2': 'Team D', 
                                     'team_1_score': 1, 'team_2_score': 1})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Match.objects.count(), 2)
        self.assertEqual(Match.objects.last().team_1, 'Team C')

    def test_match_edit_view(self):
        """
        Test that match_edit view can be accessed only by authenticated 
        user and match can be updated.
        """
        self.client.login(username='testuser', password='testpass')
        obj = Match.objects.get(id=self.match.id)
        response = self.client.post(reverse(
                 'match_edit', args=[self.match.id]), 
                 {'team_1': obj.team_1, 'team_1_score': 3,
                  'team_2': obj.team_2, 'team_2_score': obj.team_2_score})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Match.objects.get(id=self.match.id).team_1_score, 3)

    def test_match_edit_view_with_invalid_match_id(self):
        """
        Test that match_edit view returns 404 error when an invalid 
        match id is given.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('match_edit', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_delete_match(self):
        """
        Test that match_delete view can be accessed only by authenticated 
        user and match can be deleted.
        Test that match_edit view returns 404 error when a deleted match
        id is given.
        """
        # log in as the test user
        self.client.login(username='testuser', password='testpass')

        # get the URL for the delete view of the first match
        url = reverse('match_delete', args=[self.match.pk])

        # send a DELETE request to the URL
        response = self.client.delete(url)

        # check that the response has status code 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # check that the match was deleted from the database
        self.assertFalse(Match.objects.filter(pk=self.match.pk).exists())

        # try to access the edit view of the deleted match
        url = reverse('match_edit', args=[self.match.pk])
        response = self.client.get(url)

        # check that the response has status code 404 (not found)
        self.assertEqual(response.status_code, 404)

    def test_upload_match_and_ranking(self):
        """
        Test that upload_match_data view can be accessed only by 
        authenticated user and test match csv data can be uploaded. 
        Then, the ranking function will be tested consecutively.
        Test total count Match objects should be 3 (1 is from setup, 
        2 is from upload).

        Test ranking by their points and rank order.
        """
        # Login the user
        self.client.login(username='testuser', password='testpass')

        # Create a CSV file with sample data
        csv_data = b'team_1,team_1_score,team_2,team_2_score\
                 \nTeam A,2,Team B,1\nTeam C,0,Team D,0\n'
        csv_file = SimpleUploadedFile('matches.csv', csv_data, content_type=\
                                      'text/csv')

        # Submit a POST request with the CSV file
        url = reverse('upload_match_data')
        response = self.client.post(url, {'csv_file': csv_file})

        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the number of matches in the database has increased by 2
        self.assertEqual(Match.objects.count(), 3)

        url = reverse('match_ranking')
        response = self.client.get(url)
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the rendered template is correct
        self.assertTemplateUsed(response, 'match_ranking.html')
        matches = Match.objects.all()

        # Call the match_ranking function with the test data
        ranking = get_rankings(matches)

        # Check that the ranking is correct
        expected_result = [{"team_name": 'Team A', "points": 6, "rank": 1},
                           {"team_name": 'Team C', "points": 1, "rank": 2},
                           {"team_name": 'Team D', "points": 1, "rank": 3},
                           {"team_name": 'Team B', "points": 0, "rank": 4}]
        
        self.assertEqual(len(ranking), len(expected_result))
        for i, result in enumerate(expected_result):
            self.assertEqual(ranking[i]['team'], result["team_name"])
            self.assertEqual(ranking[i]['points'], result["points"])
            self.assertEqual(ranking[i]['rank'], result["rank"])

class MatchFormTestCase(TestCase):
    def test_match_form_valid(self):
        """
        Test MatchForm is valid.
        """
        form_data = {
            'team_1': 'Team A',
            'team_2': 'Team B',
            'team_1_score': 1,
            'team_2_score': 2
        }
        form = MatchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_match_form_invalid(self):
        """
        Test MatchForm is invalid because of team_1 data is empty.
        """
        form_data = {
            'team_1': '',
            'team_2': 'Team B',
            'team_1_score': 1,
            'team_2_score': 2
        }
        form = MatchForm(data=form_data)
        self.assertFalse(form.is_valid())
