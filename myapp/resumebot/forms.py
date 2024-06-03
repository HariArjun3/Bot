from django import forms


class ResumeForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    file = forms.FileField(label='Upload Resume')
