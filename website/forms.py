from django import forms
from .models import *

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['show', 'lightshow',
                  'outfit', 'dress','melody',
                  'voice', 'esc_factor', 'sexyness',
                  'douchebag', 'modulation',
                  'dress_change', 'language','plagiarism']
