from django.db import models

class tablereservation(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    date=models.DateField()
    time=models.TimeField()
    people=models.IntegerField()
    message=models.TextField()

# Create your models here.
