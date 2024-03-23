from django.db import models
from Adminapp.models import *


# Create your models here.
class Login(models.Model):
    loginid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    status=models.CharField(max_length=50)

class Servicereg(models.Model):
    providerid=models.AutoField(primary_key=True)
    email=models.CharField(max_length=50)
    phone= models.BigIntegerField()
    servicename=models.CharField(max_length=50)
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE,default="")
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE,default="")
    regdate=models.DateField(auto_now_add=True)

class Customerreg(models.Model):
    customerid=models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    addr = models.CharField(max_length=100)
    phone= models.BigIntegerField()
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE,default="")
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE,default="")
    regdate=models.DateField(auto_now_add=True)



