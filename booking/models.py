from django.db import models
from dean.models import *
# Create your models here.

class Booklist(models.Model):
    book_id=models.CharField(max_length=100,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.book_id

class Bkd_doc(models.Model):
    doct=models.ForeignKey(doctor,on_delete=models.CASCADE)
    booking=models.ForeignKey(Booklist,on_delete=models.CASCADE)
    # user_id=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.doct.name
    def total(self):
        return self.doct.con_fee