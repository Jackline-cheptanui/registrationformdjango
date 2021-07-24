from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    district=models.CharField(max_length=15)
    trainertid=models.PositiveSmallIntegerField()
    email=models.EmailField()
    course_name=models.CharField(max_length=20)
    trainerbio=models.CharField(max_length=150)
