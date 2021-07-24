from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    district=models.CharField(max_length=15)
    Studentid=models.PositiveSmallIntegerField()
    email=models.EmailField()
    