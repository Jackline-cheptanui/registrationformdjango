from django.db import models
class Course(models.Model):
    javascript=models.CharField(max_length=15)
    python=models.CharField(max_length=12)
    year=models.PositiveSmallIntegerField()
    date_of_enroll=models.DateField()
    school=models.CharField(max_length=15)
    courseid=models.PositiveSmallIntegerField()
    coursetrainer=models.CharField(max_length=12)
    
