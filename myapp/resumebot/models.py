from django.db import models
from spacy import blank


# Create your models here.

class person(models.Model):
    name = models.CharField(max_length=100)
    # marks = models.CharField(max_length=100)
    file = models.FileField(max_length=100)
