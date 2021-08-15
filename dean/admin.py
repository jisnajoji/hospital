from django.contrib import admin
from . models import *
# Register your models here.

class deptadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(dept,deptadmin)

class doctAdmin(admin.ModelAdmin):
    list_display=['name','con_fee','max_book','img','available']
    list_editable=['con_fee','max_book','img','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(doctor,doctAdmin)
