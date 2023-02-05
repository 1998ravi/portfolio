from django.contrib import admin
from .models import pr,c

# Register your models here.
admin.site.register(pr)
admin.site.register(c)

class pradmin(admin.ModelAdmin):
    list_display=['id','name','desc','Tech','image','li']
class c(admin.ModelAdmin):
    list_display=['id','n','e','com']
