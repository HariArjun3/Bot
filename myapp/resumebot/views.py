from django.shortcuts import render, HttpResponse, redirect
from .forms import MyFileForm
import PyPDF2


def home(request):
    mydata = MyFileUpload.objects.all()
    myform = MyFileForm()
    if mydata != '':
        context = {'form': myform, 'mydata': mydata}
        return render(request, 'home.html', context)
    else:
        context = {'form': myform}
        return render(request, "home.html", context)


def upload_file(request):
    if request.method == "POST":
        myform = MyFileForm(request.POST, request.FILES)
        if myform.is_valid():
            MyFileName = request.POST.get('file_name')
            MyFile = request.FILES.get('file')

            exists = MyFileUpload.objects.filter(my_file=MyFile).exists()

            if exists:
                messages.error(request, 'The file %s is already exists...!!!' % MyFile)
            else:
                # Save the uploaded file
                uploaded_file = MyFileUpload.objects.create(file_name=MyFileName, my_file=MyFile)
                uploaded_file.save()
                messages.success(request, "File uploaded successfully.")

                # Extract text from PDF if it's a PDF file
                if MyFile.content_type.startswith('application/pdf'):
                    pdf_reader = PyPDF2.PdfReader(MyFile)
                    text = ""
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        text += page.extract_text()
                    context = {'text': text}
                    return render(request, 'config_file.html', context)

    return redirect("home")