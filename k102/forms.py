from django import forms
from .models import Score

class IdForm(forms.Form):
    c_id = forms.CharField(label='', max_length=9, widget=forms.TextInput(attrs={'style': 'padding: 10px;'}))