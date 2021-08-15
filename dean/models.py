from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class dept(models.Model):
    name= models.CharField(max_length=250,unique=True)
    slug= models.SlugField(max_length=250,unique=True)
    def get_url(self):
        return reverse('doct_dept',args=[self.slug])
    def __str__(self):
        return self.name

class doctor(models.Model):
    def get_url(self):
        return reverse('details',args=[self.dept.slug,self.slug])
    def __str__(self):
        return self.name
    name= models.CharField(max_length=250,unique=True)
    slug= models.SlugField(max_length=250,unique=True)
    img= models.ImageField(upload_to='doctor')
    desc= models.TextField()
    max_book= models.IntegerField()
    available= models.BooleanField()
    con_fee= models.IntegerField()
    dept=models.ForeignKey(dept,on_delete=models.CASCADE)


