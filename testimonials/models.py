from django.db import models

class testimonial(models.Model):
    test_quets=models.TextField(max_length=300)
    test_name=models.CharField(max_length=50)
    test_designation=models.TextField()
    test_image=models.FileField(upload_to='testimonials',default=None,null=True)
    
    def __str__(self):
        return self.test_quets
# Create your models here