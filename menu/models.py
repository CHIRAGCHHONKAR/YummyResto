from django.db import models

#startermenu options
class starter(models.Model):
    starter_img=models.FileField(upload_to='menu/starter',default=None)
    starter_title=models.CharField(max_length=50)
    starter_decprition=models.TextField(max_length=100)
    starter_price=models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.starter_title
    
#breakfastmenu options
class breakfast(models.Model):
    breakfast_img=models.FileField(upload_to='menu/breakfast',default=None)
    breakfast_title=models.CharField(max_length=50)
    breakfast_decprition=models.TextField(max_length=100)
    breakfast_price=models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.breakfast_title
    
#lunchmenu options    
class lunch(models.Model):
    lunch_img=models.FileField(upload_to='menu/lunch',default=None)
    lunch_title=models.CharField(max_length=50)
    lunch_decprition=models.TextField(max_length=100)
    lunch_price=models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.lunch_title
    
#dinnermenu options
class dinner(models.Model):
    dinner_img=models.FileField(upload_to='menu/dinner',default=None)
    dinner_title=models.CharField(max_length=50)
    dinner_decprition=models.TextField(max_length=100)
    dinner_price=models.DecimalField(max_digits=5, decimal_places=2)   
    
    def __str__(self):
        return self.dinner_title         

# Create your models here.
