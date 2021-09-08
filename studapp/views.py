from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from . models import *  

# Create your views here.
def studlogin(request):
    if request.method=='POST':
        try:
            stname=request.POST['uname']
            stpass=request.POST['passw']
            ulog=Login.objects.get(username=stname,password=stpass,status='active')
            request.session['sid']=ulog.id
            return redirect('studhome')
        except:
            return render(request,'login.html',{'message':'Invalid Userdetails'})
    return render(request,'login.html')
def signup(request):
    if request.method=='POST':
        try:
            sname=request.POST['name']
            snum=request.POST['number']
            mail=request.POST['mail']
            usname=request.POST['uname']
            pswrd=request.POST['pass']
            checkuname=Login.objects.filter(username=usname).exists()
            if not checkuname:
                details=Login(username=usname,password=pswrd)
                details.save()
                request.session['sid']=details.id
                info=Registraion(name=sname,contact=snum,email=mail,loginid=details,status='active')
                info.save()
                return redirect('studhome')
            else:
                return render(request,'signup.html',{'message':'Username already exists.please signup again'})
        except:
            return render(request,'signup.html',{'message':'Error ocuuerd'})
    return render(request,'signup.html')
def admin(request):
    admin=request.session['aid']
    return render(request,'admin.html',{'alog':admin})
def studhome(request):
    logid=request.session['sid']
    udetail=Registraion.objects.get(loginid=logid)
    return render(request,'studhome.html',{'udetails':udetail})
def sprofile(request):
    stud=request.session['sid']
    log=Login.objects.get(id=stud)
    prof=Registraion.objects.get(loginid=stud)
    return render(request,'sprofile.html',{'profile':prof,'logdata':log})
def studlogout(request):
    del request.session['sid']
    return redirect('welcome')
def updprofile(request):
    updation=request.session['sid']
    if request.method=='POST':
        upname=request.POST['cname']
        upnum=request.POST['phone']
        upmail=request.POST['cmail']
        upusname=request.POST['usname']
        uppswrd=request.POST['cpass']

        Registraion.objects.filter(loginid=updation).update(name=upname,contact=upnum,email=upmail)
        prof=Registraion.objects.get(loginid=updation)

        Login.objects.filter(id=updation).update(username=upusname,password=uppswrd)
        log=Login.objects.get(id=updation)
        return render(request,'sprofile.html',{'profile':prof,'logdata':log})
    else:
        log=Login.objects.get(id=updation)
        prof=Registraion.objects.get(loginid=updation)
        return render(request,'sprofile.html',{'profile':prof,'logdata':log})
def active(request):
    logact=Login.objects.filter(status='active')
    act=Registraion.objects.filter(status='active')
    return render(request,'active.html',{'active':act,'logactive':logact})
def inactivate(request,inid): #admin inactivating a student
    Login.objects.filter(id=inid).update(status='inactive')
    Registraion.objects.filter(id=inid).update(status='inactive')
    return redirect('active')

def inactive(request):
    loginact=Login.objects.filter(status='active')
    inact=Registraion.objects.filter(status='inactive')
    return render(request,'inactive.html',{'inactive':inact,'loginactive':loginact})
def activate(request,acid):#admin activating a student
    Login.objects.filter(id=acid).update(status='active')
    Registraion.objects.filter(id=acid).update(status='active')
    return redirect('inactive')
def emailcheck(request):
    sign=request.GET['usrname']
    ucheck=Login.objects.filter(username=sign).exists()
    
    if ucheck:
        return JsonResponse({'message':True})
    else:
        return JsonResponse({'message':False})
def adminlogin(request):
    if request.method=='POST':
        try:
            uname=request.POST['aname']
            passwrd=request.POST['apassw']
            admin=AdminLogin.objects.get(adminuname=uname,adminpassword=passwrd)
            request.session['aid']=admin.id
            return redirect('admin')
        except:
            return render(request,'adminlogin.html',{'mesg':'Invalid Details'})
    return render(request,'adminlogin.html')
def alogout(request):
    del request.session['aid']
    return redirect('welcome')
def welcome(request):
    return render(request,'welcome.html')


