from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from Adminapp.models import *
from Customerapp.models import Booking
from Guestapp.models import Customerreg, Servicereg
from Serviceapp.models import Serviceregistration


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def customerhome(request):
    if "loginid" in request.session:
        return render(request, "customer/customerhome.html")
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def categoryview(request):
    if "loginid" in request.session:
        cat = Category.objects.all()
        return render(request, "customer/categoryview.html", {'category': cat})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subcatview(request, id):
    if "loginid" in request.session:
        subcat = Subcategory.objects.filter(categoryid=id)
        return render(request, "customer/subcatview.html", {'subcategory': subcat})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def servicesview(request, id):
    if "loginid" in request.session:
        sub = Serviceregistration.objects.filter(subcatid=id)
        return render(request, "customer/servicesview.html", {'services': sub})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def servicesviewmore(request,id):
    if "loginid" in request.session:
        sub = Serviceregistration.objects.get(serviceid=id)
        return render(request, "customer/serviceviewmore.html", {'services': sub})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def booking(request,id):
    if "loginid" in request.session:
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
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

def logout(request):
    if "loginid" in request.session:
        del request.session["loginid"]
        del request.session['uname']
        return redirect('/')


