from django.http import HttpResponse
from django.shortcuts import render

from Adminapp.models import *
from Customerapp.models import Booking
from Guestapp.models import Customerreg, Servicereg
from Serviceapp.models import Serviceregistration


# Create your views here.
def customerhome(request):
    return render(request, "customer/customerhome.html")


def categoryview(request):
    cat = Category.objects.all()
    return render(request, "customer/categoryview.html", {'category': cat})


def subcatview(request, id):
    subcat = Subcategory.objects.filter(categoryid=id)
    return render(request, "customer/subcatview.html", {'subcategory': subcat})


def servicesview(request, id):
    sub = Serviceregistration.objects.filter(subcatid=id)
    return render(request, "customer/servicesview.html", {'services': sub})
def servicesviewmore(request,id):
    sub = Serviceregistration.objects.get(serviceid=id)
    return render(request, "customer/serviceviewmore.html", {'services': sub})

def booking(request,id):
    if request.method == "POST":
        s=Serviceregistration.objects.get(serviceid=id)
        bob=Booking()
        bob.providerid=Servicereg.objects.get(providerid=s.providerid_id)
        bob.customerid=Customerreg.objects.get(loginid_id=request.session['loginid'])
        bob.serviceid=Serviceregistration.objects.get(serviceid=id)
        bob.eventdate=request.POST.get('eventdate')
        bob.status="Booked"
        bob.save()
        return render(request,'Customer/payment.html',{'bookinigid':bob.bookingid})


