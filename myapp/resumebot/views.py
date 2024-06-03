from django.shortcuts import render
from .forms import ResumeForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def get_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'form.html', {'name': name, 'email': email, 'file': file})
    else:
        form = ResumeForm()
    return render(request, 'form.html', {'form': form})

