from tokenize import group
from uuid import uuid4
from django.db import models

class Animals(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    weight = models.FloatField()
    characteristics = models.ManyToManyField(to="characteristics.Characteristics")
    group = models.ForeignKey(to="groups.Groups",on_delete=models.CASCADE,related_name="animals")