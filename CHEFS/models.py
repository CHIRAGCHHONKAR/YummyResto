from django.db import models


class chefs(models.Model):
    chef_image=models.FileField(upload_to="Chefs", default=None, null=True)
    chef_name=models.CharField(max_length=100)
    chef_designation=models.CharField(max_length=100)
    chef_someline=models.TextField()
    chef_twitter=models.URLField(null=True,blank=True)
    chef_facebook=models.URLField(null=True,blank=True)
    chef_instagram=models.URLField(null=True,blank=True)
    chef_linkedin=models.URLField(null=True,blank=True)
    
    def __str__(self):
        return self.chef_name
# Create your models here.
