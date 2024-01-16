from django.contrib import admin

# Register your models here.
from app.models import *


# class customize(admin.ModelAdmin):
#     list_display = ["topic_name", 'name', "url", "email"]

# class topiccustom(admin.ModelAdmin):
#     list_display = ["topic_name"]

class custom_webpage(admin.ModelAdmin):
    list_display = ["name","url","email"]




admin.site.register(Topic)
admin.site.register(Webpage,custom_webpage)
admin.site.register(Accessrecord)