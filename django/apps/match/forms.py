from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('team_1', 'team_2', 'team_1_score', 'team_2_score')
