from django.db import models

# Create your models here.
class App(models.Model):
     username = models.CharField(max_length=255, unique=True)
     role=models.CharField(max_length=100)
     bio=models.TextField(blank=True)

     def __str__(self):
        return self.username
    

