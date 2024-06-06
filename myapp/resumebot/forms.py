from django import forms
from .models import person
import re


class PersonForm(forms.ModelForm):
    # name = forms.CharField(label='Names', max_length=100)
    # file = forms.FileField()

    class Meta:
        model = person
        fields = ['name', 'file']
