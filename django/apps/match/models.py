from django.db import models

class Match(models.Model):
    team_1 = models.CharField(max_length=100)
    team_2 = models.CharField(max_length=100)
    team_1_score = models.IntegerField()
    team_2_score = models.IntegerField()

    @property
    def winner(self):
        if self.team_1_score > self.team_2_score:
            return self.team_1
        elif self.team_2_score > self.team_1_score:
            return self.team_2
        else: # tie
            return None

    @property
    def loser(self):
        if self.team_1_score < self.team_2_score:
            return self.team_1
        elif self.team_2_score < self.team_1_score:
            return self.team_2
        else: # tie
            return None