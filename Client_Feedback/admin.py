from django.contrib import admin
from Client_Feedback.models import clientfeedback


class feedback(admin.ModelAdmin):
    list_display=['name','email','subject','message']

admin.site.register(clientfeedback,feedback)
# Register your models here.
