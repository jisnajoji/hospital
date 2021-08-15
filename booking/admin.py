from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Booklist)
class bkAdmin(admin.ModelAdmin):
    list_display=['doct','date']
admin.site.register(Bkd_doc,bkAdmin)