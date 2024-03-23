from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from Adminapp.models import Location, Category, State, District
from Guestapp.models import Login, Servicereg, Customerreg


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Login.objects.filter(username=username, password=password).exists():
            loginobj = Login.objects.get(username=username, password=password)
            request.session['uname'] = loginobj.username
            request.session['loginid'] = loginobj.loginid
            role = loginobj.role
            if role == 'admin':
                return redirect('/admin/adminhome/')
            elif role == 'service providers':
                if loginobj.status == "Accepted":
                    return redirect('/service/servicehome/')
                else:
                    return HttpResponse(
                        "<script>alert('Not Verified Yet');window.location='guest/login.html';</script>")
            elif role == 'customer':
                if loginobj.status == 'confirmed':
                    return redirect('/customer/customerhome/')

            else:
                return HttpResponse(
                    "<script>alert('Not an authorized person');window.location='guest/login.html';</script>")
                # return render(request, 'guest/login.html')
        else:
            return HttpResponse(
                "<script>alert('Invalid username or password');window.location='/guest/login';</script>")
    else:
        return render(request, "guest/login.html")


def guesthome(request):
    return render(request, "guest/guesthome.html")


def servicereg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Login.objects.filter(username=username, password=password).exists():
            return HttpResponse("<script>alert('already exits');window.location='guest/login.html';</script>")
        loginobj = Login()
        loginobj.role = 'service providers'
        loginobj.status = 'requested'
        loginobj.username = username
        loginobj.password = password
        if Servicereg.objects.filter(email=request.POST.get('email')).exists():
            return HttpResponse("<script>alert('already existed mail id');window.location='guest/login.html';</script>")
        serviceobj = Servicereg()
        serviceobj.servicename = request.POST.get('servicename')
        serviceobj.phone = request.POST.get('phone')
        serviceobj.locationid = Location.objects.get(locationid=request.POST.get('location'))
        serviceobj.email = request.POST.get('email')
        loginobj.save()

        serviceobj.loginid = loginobj
        serviceobj.save()
        return HttpResponse("<script>alert('success');window.location='guest/login.html';</script>")

    state = State.objects.all()
    return render(request, "guest/servicereg.html", {'s': state})


def filldistrict(request):
    did = int(request.POST.get("did"))
    dist = District.objects.filter(stateid=did).values()
    return JsonResponse(list(dist), safe=False)


def filllocation(request):
    did = int(request.POST.get("did"))
    loc = Location.objects.filter(districtid=did).values()
    return JsonResponse(list(loc), safe=False)


def customerreg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Login.objects.filter(username=username, password=password).exists():
            return HttpResponse("<script>alert('already exits');window.location='guest/login.html';</script>")
        loginobj = Login()
        loginobj.role = 'customer'
        loginobj.status = 'confirmed'
        loginobj.username = username
        loginobj.password = password
        if Customerreg.objects.filter(email=request.POST.get('email')).exists():
            return HttpResponse("<script>alert('already existed mail id');window.location='guest/login.html';</script>")
        custobj = Customerreg()
        custobj.fname = request.POST.get('fname')
        custobj.mname = request.POST.get('mname')
        custobj.lname = request.POST.get('lname')
        custobj.phone = request.POST.get('phone')
        custobj.addr = request.POST.get('addr')
        custobj.locationid = Location.objects.get(locationid=request.POST.get('location'))
        custobj.email = request.POST.get('email')
        loginobj.save()

        custobj.loginid = loginobj
        custobj.save()
        return HttpResponse("<script>alert('success');window.location='guest/login.html';</script>")

    state = State.objects.all()
    cat = Category.objects.all()
    return render(request, "guest/customerreg.html", {'s': state, 'c': cat})
