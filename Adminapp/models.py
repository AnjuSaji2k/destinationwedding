from django.db import models


# Create your models here.
class State(models.Model):
    stateid = models.AutoField(primary_key=True)
    statename = models.CharField(max_length=50)


class District(models.Model):
    districtid = models.AutoField(primary_key=True)
    districtname = models.CharField(max_length=50)
    stateid = models.ForeignKey(State, on_delete=models.CASCADE, default="")


class Location(models.Model):
    locationid = models.AutoField(primary_key=True)
    locationname = models.CharField(max_length=50)
    districtid = models.ForeignKey(District, on_delete=models.CASCADE, default="")


class Category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=50)
    image = models.ImageField()
    desc = models.CharField(max_length=50)


class Subcategory(models.Model):
    subcatid = models.AutoField(primary_key=True)
    subcatname = models.CharField(max_length=50)
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    subimage = models.ImageField()
    desc = models.CharField(max_length=50)
