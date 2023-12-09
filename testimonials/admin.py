from django.contrib import admin
from testimonials.models import testimonial

class testimonial_admin(admin.ModelAdmin):
    list_display=['test_quets','test_name','test_designation','test_image']
    

admin.site.register(testimonial,testimonial_admin)    

# Register your models here.
