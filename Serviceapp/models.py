from django.db import models
from Adminapp.models import *
from Guestapp.models import Servicereg


# Create your models here.
class Travelreg(models.Model):
    vehicleid=models.AutoField(primary_key=True)
    vname=models.CharField(max_length=50)
    seat= models.BigIntegerField()
    image=models.ImageField()
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE,default="")
    desc=models.CharField(max_length=50)
    providerid = models.ForeignKey(Servicereg, on_delete=models.CASCADE, default="")
    rate = models.BigIntegerField()

class Cateringreg(models.Model):
    caterid=models.AutoField(primary_key=True)
    type=models.CharField(max_length=50)
    item=models.CharField(max_length=50)
    image=models.ImageField()
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE,default="")
    desc=models.CharField(max_length=50)
    providerid = models.ForeignKey(Servicereg, on_delete=models.CASCADE, default="")
    rate = models.BigIntegerField()

class Destinationreg(models.Model):
    destid=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=50)
    image=models.ImageField()
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE,default="")
    desc=models.CharField(max_length=100)
    providerid = models.ForeignKey(Servicereg, on_delete=models.CASCADE, default="")
    rate = models.BigIntegerField()


class Serviceregistration(models.Model):
    serviceid=models.AutoField(primary_key=True)
    servicename=models.CharField(max_length=50)
    image=models.ImageField()
    subcatid = models.ForeignKey(Subcategory, on_delete=models.CASCADE,default="")
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE,default="")
    desc=models.CharField(max_length=100)
    providerid = models.ForeignKey(Servicereg, on_delete=models.CASCADE, default="")
    rate = models.BigIntegerField()




