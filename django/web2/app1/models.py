from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    contactnumber=models.CharField(max_length=12)
   
   
    def __str__(self):
         return self.username
    
class TeamMember(models.Model):
     username = models.CharField(max_length=255, unique=True)
     role=models.CharField(max_length=100)
     bio=models.TextField(blank=True)
     dateOfJoining=models.DateField()

     def __str__(self):
        return self.username
     
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    contact_date = models.DateField()   


class Admission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contactnumber=models.CharField(max_length=12)
    dateOfAdmission=models.DateField()
     

