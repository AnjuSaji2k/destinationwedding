import smtplib
from email.message import EmailMessage

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from Adminapp.models import *
from Guestapp.models import Servicereg, Login


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminhome(request):
    if "loginid" in request.session:
        return render(request, "Admin/adminhome.html")
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")



# state regis
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def statereg(request):
    if "loginid" in request.session:
        if request.method == 'POST':
            statename = request.POST.get('statename')
            state_obj = State()
            if State.objects.filter(statename=statename).exists():
                return HttpResponse("<script>alert('Duplicate...');window.location='/admin/statereg/';</script>")
            state_obj.statename = statename
            state_obj.save()
            return HttpResponse("<script>alert('State Inserted...');window.location='/admin/stateview/';</script>")

        return render(request, "Admin/statereg.html")
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")



def stateview(request):
    if "loginid" in request.session:
        state = State.objects.all()
        return render(request, "Admin/stateview.html", {'state': state})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def statedelete(request, id):
    if "loginid" in request.session:
        state = State.objects.get(stateid=id)
        state.delete()
        return stateview(request)
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def stateedit(request, id):
    if "loginid" in request.session:
        if request.method == 'POST':
            statename = request.POST.get('statename')

            state = State.objects.get(stateid=id)
            state.statename = statename
            state.save()
            return stateview(request)
        else:
            state = State.objects.get(stateid=id)
            return render(request, "Admin/stateedit.html", {'st': state})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def districtreg(request):
    if "loginid" in request.session:
        if request.method == 'POST':
            districtname = request.POST.get('district')
            statename = request.POST.get('statename')
            dist_obj = District()
            if District.objects.filter(districtname=districtname).exists():
                return HttpResponse("<script>alert('Duplicate...');window.location='/admin/districtreg/';</script>")
            dist_obj.districtname = districtname
            dist_obj.stateid = State.objects.get(stateid=statename)
            dist_obj.save()
            return HttpResponse("<script>alert('District Registered');window.location='/admin/districtview/';</script>")
        else:
            s = State.objects.all()
            return render(request, "Admin/districtreg.html", {'s': s})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def districtview(request):
    if "loginid" in request.session:
        state = State.objects.all()
        dist = District.objects.all()  # select * from Department
        return render(request, "Admin/districtview.html", {'state': state, 'dist': dist})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def districtdelete(request, id):
    if "loginid" in request.session:
        dist = District.objects.get(districtid=id)
        dist.delete()
        return districtview(request)
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def districtedit(request, id):
    if "loginid" in request.session:
        if request.method == 'POST':
            dname = request.POST.get('district')
            dist = District.objects.get(districtid=id)
            dist.districtname = dname
            dist.save()
            return districtview(request)
        else:
            state = State.objects.all()
            dist = District.objects.get(districtid=id)
            return render(request, "Admin/districtedit.html", {'dist': dist, 'state': state})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def locationreg(request):
    if "loginid" in request.session:
        if request.method == 'POST':
            districtname = request.POST.get('district')
            statename = request.POST.get('statename')
            loc = request.POST.get('location')
            loc_obj = Location()
            if Location.objects.filter(locationname=loc).exists():
                return HttpResponse("<script>alert('Duplicate...');window.location='/admin/locationreg/';</script>")
            loc_obj.locationname = loc
            loc_obj.districtid = District.objects.get(districtid=districtname)
            loc_obj.stateid = State.objects.get(stateid=statename)
            loc_obj.save()
            return HttpResponse("<script>alert('Location Registered');window.location='/admin/locationreg/';</script>")
        s = State.objects.all()
        return render(request, "Admin/locationreg.html", {'s': s})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


def filldistrict(request):
    did = int(request.POST.get("did"))
    dist = District.objects.filter(stateid=did).values()
    return JsonResponse(list(dist), safe=False)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def locationview(request):
    if "loginid" in request.session:
        loc = Location.objects.all()
        state = State.objects.all()
        return render(request, "Admin/locationview.html", {'state': state, 'loc': loc})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


def filllocation(request):
    did = int(request.POST.get("did"))
    loc = Location.objects.filter(districtid=did).values()
    return JsonResponse(list(loc), safe=False)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def locationedit(request, id):
    if "loginid" in request.session:
        if request.method == 'POST':
            lname = request.POST.get('location')
            dname = request.POST.get('district')
            location = Location.objects.get(locationid=id)
            location.locationname = lname
            location.districtid = District.objects.get(districtid=dname)
            location.save()
            return locationview(request)
        else:
            state = State.objects.all()
            loc = Location.objects.get(locationid=id)
            return render(request, "Admin/locationedit.html", {'location': loc, 'state': state})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def locationdelete(request, id):
    if "loginid" in request.session:
        loc = Location.objects.get(locationid=id)
        loc.delete()
        return locationview(request)
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def categoryreg(request):
    if "loginid" in request.session:
        if request.method == "POST":
            categoryname = request.POST.get('categoryname')
            image = request.POST.get('image')
            desc = request.POST.get('desc')
            cat_obj = Category()
            if Category.objects.filter(categoryname=categoryname, image=image, desc=desc).exists():
                return HttpResponse("<script>alert('Duplicate..');window.location='/Admin/category/';</script>")
            cat_obj.categoryname = categoryname
            cat_obj.image = request.FILES['image']
            cat_obj.desc = desc
            cat_obj.save()

            return HttpResponse("<script>alert('Category Inserted...');window.location='/admin/categoryview/';</script>")

        return render(request, "Admin/categoryreg.html")
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subcategoryreg(request):
    if "loginid" in request.session:
        if request.method == "POST":
            subcategoryname = request.POST.get('categoryname')
            desc = request.POST.get('subcategorydesc')
            subcat_obj = Subcategory()
            if Subcategory.objects.filter(subcatname=subcategoryname).exists():
                return HttpResponse("<script>alert('Duplicate..');window.location='/Admin/subcategoryreg/';</script>")
            subcat_obj.subcatname = subcategoryname

            if len(request.FILES) == 1:
                subcat_obj.subimage = request.FILES.get("subcategoryimage")
            else:
                subcat_obj.subimage = 'default.jpg'

            subcat_obj.desc = desc
            subcat_obj.categoryid = Category.objects.get(categoryid=request.POST.get('category'))
            subcat_obj.save()
            return HttpResponse(
                "<script>alert('subcategory Inserted...');window.location='/admin/subcategoryreg/';</script>")

        cat = Category.objects.all()
        return render(request, "Admin/subcatreg.html", {'category': cat})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def categoryview(request):
    if "loginid" in request.session:
        cat = Category.objects.all()
        return render(request, "Admin/categoryview.html", {'category': cat})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subcatview(request):
    if "loginid" in request.session:
        cat = Category.objects.all()
        subcat = Subcategory.objects.all()
        return render(request, "Admin/subcategoryview.html", {'subcat': subcat, 'category': cat})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")


def fillcategory(request):
    did = int(request.POST.get("did"))
    subcat = Subcategory.objects.filter(categoryid=did).values()
    return JsonResponse(list(subcat), safe=False)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subcatdelete(request, id):
    if "loginid" in request.session:
        subcat = Subcategory.objects.get(subcatid=id)
        subcat.delete()
        return subcatview(request)
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subcatedit(request, id):
    if "loginid" in request.session:
        if request.method == 'POST':

            subname = request.POST.get('categoryname')
            desc = request.POST.get('subcategorydesc')
            subcat = Subcategory.objects.get(subcatid=id)
            subcat.subcatname = subname
            subcat.categoryid = Category.objects.get(categoryid=request.POST.get('catname'))
            subcat.desc = desc
            if len(request.FILES) != 0:
                subcat.subimage = request.FILES['newimage']
            else:
                subcat.subimage = request.POST.get('imageold')
            subcat.save()
            return subcatview(request)
        else:
            cat = Category.objects.all()
            subcat = Subcategory.objects.get(subcatid=id)
            return render(request, "Admin/subcatedit.html", {'subcat': subcat, 'category': cat})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def categorydelete(request, id):
    if "loginid" in request.session:
        cat = Category.objects.get(categoryid=id)
        cat.delete()
        return categoryview(request)
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def categoryedit(request, id):
    if "loginid" in request.session:
        if request.method == 'POST':
            cname = request.POST.get('categoryname')
            desc = request.POST.get('desc')
            category = Category.objects.get(categoryid=id)
            category.categoryname = cname
            category.desc = desc
            if len(request.FILES) == 0:
                category.image = request.POST.get("imageid")
            else:
                category.image = request.FILES["image"]
            category.save()
            return categoryview(request)
        cat = Category.objects.get(categoryid=id)
        return render(request, "Admin/categoryedit.html", {'category': cat})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def servicerrequest(request):
    if "loginid" in request.session:
        ser = Servicereg.objects.filter(loginid__status="requested")
        return render(request, "Admin/servicerequestview.html", {'ser': ser})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def serviceraccept(request, id):
    if "loginid" in request.session:
        login = Login.objects.get(loginid=id)
        obj = Servicereg.objects.get(loginid=id)
        email = obj.email
        login.status = "Accepted"
        login.save()

        # mail
        msg = EmailMessage()
        msg.set_content('Request Accepted')
        msg['Subject'] = "Registration Request"
        msg['from'] = 'anjusaji2k@gmail.com'
        msg['To'] = {email}
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('anjusaji2k@gmail.com', 'zdcbadbxinbxseid')
            smtp.send_message(msg)
        return HttpResponse("<script>alert('Mail Sended...');window.location='/admin/servicerequestview/';</script>")
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def servicerreject(request, id):
    if "loginid" in request.session:
        login = Login.objects.get(loginid=id)
        obj = Servicereg.objects.get(loginid=id)
        email = obj.email
        login.status = "Rejected"
        login.save()

        # mail
        msg = EmailMessage()
        msg.set_content('Request Rejected')
        msg['Subject'] = "Registration Request"
        msg['from'] = 'anjusaji2k@gmail.com'
        msg['To'] = {email}
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('anjusaji2k@gmail.com', 'zdcbadbxinbxseid')
            smtp.send_message(msg)
        return HttpResponse("<script>alert('Mail Sended...');window.location='/admin/servicerequestview/';</script>")
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def serviceacceptview(request):
    if "loginid" in request.session:
        ser = Servicereg.objects.filter(loginid__status="accepted")
        return render(request, "Admin/serviceacceptview.html", {'ser': ser})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def servicerejectview(request):
    if "loginid" in request.session:
        ser = Servicereg.objects.filter(loginid__status="rejected")
        return render(request, "Admin/servicerejectview.html", {'ser': ser})
    else:
        return HttpResponse("<script>alert('Login First');window.location='/';</script>")

def logout(request):
    if "loginid" in request.session:
        del request.session["loginid"]
        del request.session['uname']
        return redirect('/')
