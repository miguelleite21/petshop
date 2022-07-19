from django.db import models
from uuid import uuid4

class Groups(models.Model):
    name = models.CharField(max_length=50,unique=True)
    scientific_name = models.CharField(max_length=50)

    