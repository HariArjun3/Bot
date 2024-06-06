from django.shortcuts import render, HttpResponse
from .forms import PersonForm
import os
from django.shortcuts import render
from django.conf import settings
from PyMuPDF import pdfplumber  # or import pdfplumber


# Create your views here.

def home(request):
    return render(request, 'home.html')


def upload_pdf(request):
    extracted_text = None
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']

    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_file.name)

    with open(pdf_path, 'wb+') as destination:
        for chunk in pdf_file.chunks():
            destination.write(chunk)

    extracted_text = extract_text_from_pdf(pdf_path)
    os.remove(pdf_path)  # Clean up uploaded file after extraction

    return render(request, 'extractor/upload.html', {'extracted_text': extracted_text})


def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text
