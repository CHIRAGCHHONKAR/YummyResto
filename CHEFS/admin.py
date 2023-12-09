from django.contrib import admin
from CHEFS.models import chefs

class admin_chefs(admin.ModelAdmin):
    list_display=['chef_name','chef_designation','chef_someline','chef_twitter','chef_facebook','chef_instagram','chef_linkedin','chef_image']
    
admin.site.register(chefs,admin_chefs)    
# Register your models here.
