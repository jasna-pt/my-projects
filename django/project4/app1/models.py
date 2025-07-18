from django.db import models

# Create your models here.
class Jas(models.Model):
    name = models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    admission_date=models.IntegerField()