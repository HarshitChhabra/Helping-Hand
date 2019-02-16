"""helping_hand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from fundraiser import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('bdr',views.bloodDonorRegistration,name='bdr'),
    path('test',views.bloodDonorsDisplay,name='donorsDisp'),
    path('eduhelp',views.eduHelpRegistration,name='eduhelp'),
    path('edudonor',views.eduDonorRegistration,name='edudonor'),
    path('fundraiser/',include('fundraiser.urls')),
    path('organdonor/', views.OrganDonorView, name='organDonor'),
    path('organDonorList', views.organDispView, name='organdisp'),
    path('helporphans',views.orphanageHelpView,name='orphanagehelp'),
    path('oldagehelp',views.oldageHelpView,name='oldagehelp'),
    path('signup',views.signupView,name='signup'),
    path('fundraiserreg',views.fundraiserRegView,name='fundraiserReg'),
    path('ongoingfundraisers',views.ongoingfundraisersView,name='ongoingfundraisers'),
    path('ngoverification',views.ngoVerificationList.as_view(),name='pendingfundraisers'),
    path('ngoverification/<int:pk>',views.ngoVerification.as_view(),name='ngoVerifyPage')
]
