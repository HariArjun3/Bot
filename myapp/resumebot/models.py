from django.db import models
from spacy import blank


# Create your models here.

class MyFileUpload(models.Model):
    file_name=models.CharField(max_length=50)
    my_file=models.FileField()
