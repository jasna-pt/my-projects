from django.db import models

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.name
    

class Message(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return self.name
    



