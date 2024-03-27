from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from Adminapp.models import *
from Guestapp.models import Servicereg
from Serviceapp.models import *


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if "loginid" in request.session:
        return render(request, "service/servicehome.html")
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


def travelreg(request):
    if request.method == "POST":
        vname = request.POST.get('name')
        seats = request.POST.get('seats')
        rate = request.POST.get('rate')
        desc = request.POST.get('desc')
        subcategory = request.POST.get('subcategory')
        trvl_obj = Travelreg()
        if Travelreg.objects.filter(vname=vname, seat=seats).exists():
            return HttpResponse("<script>alert('Duplicated Entry..');window.location='/service/travelreg/';</script>")
        trvl_obj.vname = vname
        trvl_obj.seat = seats
        trvl_obj.rate = rate
        trvl_obj.desc = desc
        trvl_obj.image = request.FILES['image']
        trvl_obj.subcatid = Subcategory.objects.get(subcatid=(subcategory))
        trvl_obj.locationid = Location.objects.get(locationid=request.POST.get('location'))
        pro = Servicereg.objects.get(loginid=request.session['loginid'])
        provider = pro.providerid
        trvl_obj.providerid = Servicereg.objects.get(providerid=provider)
        trvl_obj.save()
        return HttpResponse("<script>alert('Service Inserted...');window.location='/service/travelreg/';</script>")

    cat = Category.objects.all()
    state = State.objects.all()
    return render(request, "service/travelreg.html", {'st': state, 'category': cat})


def filldistrict(request):
    did = int(request.POST.get("did"))
    dist = District.objects.filter(stateid=did).values()
    return JsonResponse(list(dist), safe=False)


def filllocation(request):
    did = int(request.POST.get("did"))
    loc = Location.objects.filter(districtid=did).values()
    return JsonResponse(list(loc), safe=False)


def travelview(request):
    trvlview = Travelreg.objects.all()
    return render(request, "service/travelview.html", {'trvl': trvlview})


def traveldelete(request, id):
    trvl = Travelreg.objects.get(vehicleid=id)
    trvl.delete()
    return travelview(request)


def cateringreg(request):
    if request.method == "POST":
        item = request.POST.get('itemname')
        type = request.POST.get('type')
        rate = request.POST.get('rate')
        desc = request.POST.get('desc')
        categoryname = request.POST.get('categoryname')
        cater_obj = Cateringreg()
        if Cateringreg.objects.filter(item=item, type=type).exists():
            return HttpResponse("<script>alert('Duplicated Entry..');window.location='/service/cateringreg/';</script>")
        cater_obj.item = item
        cater_obj.type = type
        cater_obj.rate = rate
        cater_obj.desc = desc
        cater_obj.image = request.FILES['image']
        cater_obj.categoryid = Category.objects.get(categoryid=(categoryname))
        cater_obj.locationid = Location.objects.get(locationid=request.POST.get('location'))
        pro = Servicereg.objects.get(loginid=request.session['loginid'])
        provider = pro.providerid
        cater_obj.providerid = Servicereg.objects.get(providerid=provider)
        cater_obj.save()
        return HttpResponse("<script>alert('Service Inserted...');window.location='/service/cateringreg/';</script>")
    cat = Category.objects.all()
    state = State.objects.all()
    return render(request, "service/cateringreg.html", {'category': cat, 'st': state})


def traveledit(request, id):
    if request.method == 'POST':
        vname = request.POST.get('name')
        seats = request.POST.get('seats')
        rate = request.POST.get('rate')
        desc = request.POST.get('desc')
        categoryid = request.POST.get('categoryname')
        t = Travelreg.objects.get(vehicleid=id)
        t.vname = vname
        t.seat = seats
        t.rate = rate
        t.desc = desc
        t.categoryid = Category.objects.get(categoryid=categoryid)
        if len(request.FILES) != 0:
            t.image = request.FILES['imagenew']
        else:
            t.image = request.POST.get('imageold')

        t.locationid = Location.objects.get(locationid=request.POST.get('location'))

        t.save()
        return travelview(request)
    else:
        trvl = Travelreg.objects.get(vehicleid=id)
        state = State.objects.all()
        district = District.objects.filter(stateid=trvl.locationid.districtid.stateid)
        loc = Location.objects.filter(districtid=trvl.locationid.districtid)
        category = Category.objects.all()
        return render(request, "service/traveledit.html",
                      {'trvl': trvl, 'state': state, 'category': category, 'dist': district, 'loc': loc})


def cateringview(request):
    cat = Cateringreg.objects.all()
    return render(request, "service/cateringview.html", {'catering': cat})


def cateringdelete(request, id):
    cater = Cateringreg.objects.get(caterid=id)
    cater.delete()
    return cateringview(request)


def cateringedit(request, id):
    if request.method == 'POST':
        name = request.POST.get('itemname')
        type = request.POST.get('type')
        rate = request.POST.get('rate')
        desc = request.POST.get('desc')
        categoryid = request.POST.get('categoryname')
        c = Cateringreg.objects.get(caterid=id)
        c.item = name
        c.type = type
        c.rate = rate
        c.desc = desc
        c.categoryid = Category.objects.get(categoryid=categoryid)
        if len(request.FILES) != 0:
            c.image = request.FILES['imagenew']
        else:
            c.image = request.POST.get('imageold')
        c.locationid = Location.objects.get(locationid=request.POST.get('location'))
        c.save()
        return cateringview(request)
    else:
        cater = Cateringreg.objects.get(caterid=id)
        state = State.objects.all()
        district = District.objects.filter(stateid=cater.locationid.districtid.stateid)
        loc = Location.objects.filter(districtid=cater.locationid.districtid)
        category = Category.objects.all()
        return render(request, "service/cateringedit.html",{'cater': cater, 'state': state, 'category': category, 'dist': district, 'loc': loc})


def destinationreg(request):
    if request.method == "POST":
        dname = request.POST.get('name')
        rate = request.POST.get('rate')
        desc = request.POST.get('desc')
        categoryname = request.POST.get('categoryname')
        destobj = Destinationreg()
        if Destinationreg.objects.filter(dname=dname).exists():
            return HttpResponse(
                "<script>alert('Duplicated Entry..');window.location='/service/destinationreg/';</script>")
        destobj.dname = dname
        destobj.rate = rate
        destobj.desc = desc
        destobj.image = request.FILES['image']
        destobj.categoryid = Category.objects.get(categoryid=(categoryname))
        destobj.locationid = Location.objects.get(locationid=request.POST.get('location'))
        pro = Servicereg.objects.get(loginid=request.session['loginid'])
        provider = pro.providerid
        destobj.providerid = Servicereg.objects.get(providerid=provider)
        destobj.save()
        return HttpResponse("<script>alert('Service Inserted...');window.location='/service/destinationreg/';</script>")
    cat = Category.objects.all()
    state = State.objects.all()
    return render(request, "service/destinationreg.html", {'category': cat, 'st': state})


def destinationview(request):
    dest = Destinationreg.objects.all()
    return render(request, "service/destinationview.html", {'destination': dest})


def destinationdelete(request, id):
    dest = Destinationreg.objects.get(destid=id)
    dest.delete()
    return destinationview(request)


def destinationedit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        rate = request.POST.get('rate')
        desc = request.POST.get('desc')
        categoryid = request.POST.get('categoryname')
        d = Destinationreg.objects.get(destid=id)
        d.dname = name
        d.rate = rate
        d.desc = desc
        d.categoryid = Category.objects.get(categoryid=categoryid)
        if len(request.FILES) != 0:
            d.image = request.FILES['imagenew']
        else:
            d.image = request.POST.get('imageold')

        d.locationid = Location.objects.get(locationid=request.POST.get('location'))

        d.save()
        return destinationview(request)
    else:
        dest = Destinationreg.objects.get(destid=id)
        state = State.objects.all()
        district = District.objects.filter(stateid=dest.locationid.districtid.stateid)
        loc = Location.objects.filter(districtid=dest.locationid.districtid)
        category = Category.objects.all()
        return render(request, "service/destinationedit.html",
                      {'destination': dest, 'state': state, 'category': category, 'dist': district, 'loc': loc})


def fillcategory(request):
    did = int(request.POST.get("did"))
    subcat = Subcategory.objects.filter(categoryid=did).values()
    return JsonResponse(list(subcat), safe=False)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def serviceregistration(request):
    if "loginid" in request.session:
        if request.method == "POST":
            pro = request.session['loginid']
            idr = Servicereg.objects.get(loginid=pro)
            # return HttpResponse(pro)
            provider =idr.providerid
            sname = request.POST.get('servname')
            desc = request.POST.get('desc')
            rate = request.POST.get('rate')
            subcategory = request.POST.get('subcategory')
            ser_obj = Serviceregistration()
            if Serviceregistration.objects.filter(servicename=sname, desc=desc).exists():
                return HttpResponse(
                    "<script>alert('Duplicated Entry..');window.location='/service/serviceregistration/';</script>")
            ser_obj.servicename = sname
            ser_obj.desc = desc
            ser_obj.image = request.FILES['image']
            ser_obj.subcatid = Subcategory.objects.get(subcatid=(subcategory))
            ser_obj.locationid = Location.objects.get(locationid=request.POST.get('location'))
            ser_obj.providerid = Servicereg.objects.get(providerid=provider)
            ser_obj.rate = rate
            ser_obj.save()
            return HttpResponse(
                "<script>alert('Service Inserted...');window.location='/service/serviceregistration/';</script>")

        cat = Category.objects.all()
        state = State.objects.all()
        return render(request, "service/serviceregistration.html", {'st': state, 'category': cat})

    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def serviceregisterview(request):
    if "loginid" in request.session:
        cat = Category.objects.all()
        ser = Serviceregistration.objects.all()
        return render(request, "service/serviceregisterview.html", {'services': ser, 'category': cat})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


def logout(request):
    if "loginid" in request.session:
        del request.session["loginid"]
        del request.session['uname']
        return redirect('/')