from django.contrib import admin
from Table_Reservation.models import tablereservation

class reservation(admin.ModelAdmin):
     list_display=['name','email','phone','date','time','people','message']

admin.site.register(tablereservation,reservation)

# Register your models here.
