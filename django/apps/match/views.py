import csv
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect

from .forms import MatchForm
from .models import Match
from .utils import get_rankings

def index(request):
    """
    Main page of the system.
    """
    return redirect('match_list')

# function-based view to display all matches
def match_list(request):
    """
    Display all matches in the database.
    """
    matches = Match.objects.all()
    return render(request, 'match_list.html', {'matches': matches})

# function-based view to display create match form
@login_required
def match_new(request):
    """
    Display the create match form.
    Only logged-in users can access this endpoint.
    """
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            match.save()
            return redirect('match_list')
    else:
        form = MatchForm()

    return render(request, 'match_edit.html', {'form': form, \
                                               'header_label': "Add New Match"})

# function-based view to display update match form
@login_required
def match_edit(request, pk):
    """
    Display the update match form for the given primary key.
    Only logged-in users can access this endpoint.
    """
    match = get_object_or_404(Match, pk=pk)
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            match = form.save(commit=False)
            match.save()
            return redirect('match_list')
    else:
        form = MatchForm(instance=match)

    return render(request, 'match_edit.html', {'form': form, \
                                               'header_label': "Edit Match"})

# function-based view to delete match data
@login_required
def match_delete(request, pk):
    """
    Delete match data for the given primary key.
    Only logged-in users can access this endpoint.
    """
    match = get_object_or_404(Match, pk=pk)
    match.delete()
    return redirect('match_list')

# function-based view to upload match csv data
@login_required
def upload_match_data(request):
    """
    Display upload match data form that allows uploading of match data 
    CSV file. Only logged-in users can access this endpoint.
    """
    if request.method != 'POST':
        return render(request, 'upload_match_data.html')
    csv_file = request.FILES.get('csv_file')
    if not csv_file:
        return render(request, 'upload_match_data.html', \
                      {'error': 'Please select a file to upload.'})

    if not csv_file.name.endswith('.csv'):
        return render(request, 'upload_match_data.html', \
                      {'error': 'Please upload a CSV file.'})

    errors = []
    csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
    next(csv_data)  # skip header row

    for row in csv_data:
        form = MatchForm({
             'team_1': row[0],
             'team_1_score': row[1],
             'team_2': row[2],
             'team_2_score': row[3]})
        
        if form.is_valid():
            try:
                form.save()
            except ValidationError as e:
                errors.append(f"Error saving match: {str(e)}")
        else:
            errors.append(f"Invalid match data: {form.errors}")
    if errors:
        return render(request, 'upload_match_data.html', \
                      {'error': "\n".join(errors)})
    return redirect('match_list')

# function-based view to display match ranking form
def match_ranking(request):
    """
    The core ranking logic of this form has separated into utils.py
    """
    matches = Match.objects.all()
    return render(request, 'match_ranking.html', \
                  {'ranking_data': get_rankings(matches)})