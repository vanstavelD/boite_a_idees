from django import forms
from .models import Idee

class IdeeForm(forms.ModelForm):
    class Meta:
        model = Idee
        fields = ['formulation', 'detail']
