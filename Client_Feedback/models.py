from django.db import models


class clientfeedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=1000)
    message=models.TextField()
# Create your models here.
