from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from . import forms
from . import models
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect
from twilio.rest import Client
from django.views.generic import UpdateView,ListView
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    g=GeoIP2()
    print(g.country('google.com'))
    print(g.city('183.83.12.234'))
    if request.method=='GET':
        if request.GET.get('signout'):
            print(request.META)
            logout(request)
            return HttpResponseRedirect('http://127.0.0.1:8000')
            #return render(request,'fundraiser/index.html')
        if request.GET.get('getsignup'):
            return signupView(request)
        #print('got post',request.GET.get('getsignup'))
    else:
        if 'signout' in request.POST:
            print('got signout req')
            logout(request)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    fundraisers=models.Fundraisers.objects.filter(verification=True)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return render(request,"fundraiser/index.html",{'fundraisers':fundraisers})

def bloodDonorRegistration(request):
    print(request)
    if request.user.is_authenticated==False:
        return userLoginView(request)
    form=forms.bloodDonorForm()
    if request.method=='POST':
        form=forms.bloodDonorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'fundraiser/bdReg.html',{'bdReg':form})

def bloodDonorsDisplay(request):
    if 'bloodgroup' in request.POST:
        selectedbg=request.POST['bloodgroup']
        name=request.POST['name']
        phnum=request.POST['phnumber']
        donors=models.BloodDonors.objects.filter(bloodgroup=selectedbg)
        if(len(donors)>0):
            account_sid = "AC1bce3a33ed8452a928006c09168675d1"
            auth_token = "77679537dfe41f79ff6ff85bb3708279"
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body="There's an urgent requirement for the blood "+selectedbg+' Name: '+name+' Phone number: '+phnum,
                to="+918125799791",
                from_="+19403292905")
            print(message.sid)
        return render(request, 'fundraiser/bloodDonors.html', {'donors': donors})
    else:
        return render(request,'fundraiser/bloodDonors.html')

def eduDonorRegistration(request):
    if request.user.is_authenticated==False:
        return userLoginView(request)
    if request.user.is_authenticated==False:
        return userLoginView(request)
    print('hello')
    current_user = request.user
    form=forms.eduDonorForm(initial={'user':current_user})
    if 'getReqs' in request.POST:
        reqs=models.eduDonationReq.objects.all()
        return render(request,'fundraiser/eduReqDisp.html',{'reqs':reqs})
    if request.method=='POST':
        form=forms.eduDonorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('invalid')
    return render(request,'fundraiser/eduDonorReg.html',{'form':form})

def eduHelpRegistration(request):
    if request.user.is_authenticated==False:
        return userLoginView(request)
    if request.user.is_authenticated==False:
        return signupView(request)
        #return userLoginView(request)
    form=forms.eduHelpForm()
    if request.method=='POST':
        form=forms.eduHelpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'fundraiser/eduHelp.html',{'form':form})

def orphanageHelpView(request):
    return render(request,'fundraiser/orphanageHelp.html')

def oldageHelpView(request):
    return render(request,'fundraiser/oldagehelp.html')

def OrganDonorView(request):
    if request.user.is_authenticated==False:
        return userLoginView(request)
    form=forms.OrganDonorForm()
    if request.method=='POST':
        form=forms.OrganDonorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'fundraiser/organdonor.html',{'org_don':form})

def organDispView(request):
    if request.user.is_authenticated==False:
        return userLoginView(request)
    if request.method=='POST':
        if 'organpart' in request.POST:
            reqorgan=request.POST['organpart']
            print(reqorgan)
            alldonors=models.OrganDonors.objects.all()
            tempdnrs=models.OrganDonors.objects
            idlst=[]
            templst=[]
            for obj in alldonors:
                flag=0
                for org in obj.Parts_you_want_to_donate:
                    if org==reqorgan:
                        flag=1
                        break
                if flag==0:
                    templst.append(obj)
                    idlst.append(obj.id)

            alldonors=models.OrganDonors.objects.exclude(id__in=[tempid for tempid in idlst])
            #print(len(alldonors))
            if len(alldonors)==0:
                print('hello')
                return render(request, 'fundraiser/organDisp.html', {'nonefound': "1"})
            return render(request,'fundraiser/organDisp.html',{'donorlist':alldonors})

    return render(request,'fundraiser/organDisp.html')

def fundraiserRegView(request):
    form=forms.NewFundRaiserForm()
    if request.method=='POST':
        form=forms.NewFundRaiserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'fundraiser/fundraiserReg.html',{'successful':"1"})
    return render(request,'fundraiser/fundraiserReg.html',{'fundraiserForm':form})

def ongoingfundraisersView(request):
    fundraisers=models.Fundraisers.objects.filter(verification=True)
    if(len(fundraisers)>0):
        return render(request,'fundraiser/ongoingfundraisers.html',{'fundraiserList':fundraisers})
    return render(request,'fundraiser/ongoingfundraisers.html')

def signupView(request):
    form=forms.userSignupForm()
    if request.method=='POST':

        redirectlink = request.META.get('HTTP_REFERER')
        form=forms.userSignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            print(user)
            request.session.set_expiry(86400)
            login(request, user)
            return HttpResponseRedirect('http://127.0.0.1:8000')
    return render(request,'fundraiser/index.html',{'signupform':form})

def userLoginView(request):
    form=forms.userloginForm()
    redirectlink=request.META.get('HTTP_REFERER')
    print('check123',request.POST)
    if request.method=='POST':
        form=forms.userloginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    request.session.set_expiry(86400)
                    login(request, user)
                    return HttpResponseRedirect(redirectlink)
            else:
                print('wrong credentials')
    return render(request,'fundraiser/index.html',{'userloginform':form})

class ngoVerification(UpdateView):
    template_name = 'fundraiser/ngoverification.html'
    model=models.Fundraisers
    fields = ['verification']
    context_object_name = 'objectToBeVerified'
    success_url = reverse_lazy('pendingfundraisers')

class ngoVerificationList(ListView):
    model=models.Fundraisers
    queryset = models.Fundraisers.objects.filter(verification=False)
    template_name = 'fundraiser/ngoverificationList.html'
    context_object_name = 'pendingFundraisersList'