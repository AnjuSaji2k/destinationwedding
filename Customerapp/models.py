from django.db import models

from Guestapp.models import *
from Serviceapp.models import *


# Create your models here.
class Booking(models.Model):
    bookingid = models.AutoField(primary_key=True)
    providerid = models.ForeignKey(Servicereg,on_delete=models.CASCADE)
    customerid = models.ForeignKey(Customerreg, on_delete=models.CASCADE)
    serviceid = models.ForeignKey(Serviceregistration, on_delete=models.CASCADE)
    bookingdate= models.DateField(auto_now_add=True)
    eventdate = models.DateField()
    status= models.CharField(max_length=50)