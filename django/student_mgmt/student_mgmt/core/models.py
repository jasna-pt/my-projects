from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    Course=models.CharField(max_length=100)
    Join_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

