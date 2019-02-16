from django.urls import path
from . import views

app_name='fundraiser'

urlpatterns=[
    path('',views.bloodDonorRegistration,name='bdr'),#blood donor registration
]