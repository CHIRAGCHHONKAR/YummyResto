from django.contrib import admin
from menu.models import starter,breakfast,lunch,dinner

class starteradmin(admin.ModelAdmin):
    list_display=('starter_title','starter_decprition','starter_price','starter_img')

class breakfastadmin(admin.ModelAdmin):
    list_display=('breakfast_title','breakfast_decprition','breakfast_price','breakfast_img')

class lunchadmin(admin.ModelAdmin):
    list_display=('lunch_title','lunch_decprition','lunch_price','lunch_img')

class dinneradmin(admin.ModelAdmin):
    list_display=('dinner_title','dinner_decprition','dinner_price','dinner_img')            
    
admin.site.register(starter,starteradmin)
admin.site.register(breakfast,breakfastadmin)
admin.site.register(lunch,lunchadmin)
admin.site.register(dinner,dinneradmin)

# Register your models here.
