from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings
import django.contrib.auth as authlib
# Create your models here.

class BloodDonors(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.DecimalField(max_digits=10,decimal_places=0)
    location=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    bloodgroups=(('O+ve','O+ve'),('O-ve','O-ve'),('A+ve','A+ve'),('A-ve','A-ve'),('B+ve','B+ve'),('B-ve','B-ve'),('AB+ve','AB+ve'),('AB-ve','AB-ve'))
    bloodgroup=models.CharField(max_length=5,choices=bloodgroups)

class eduDonors(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.DecimalField(max_digits=10,decimal_places=0)
    location=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    notification=models.BooleanField(default=False)
    user = models.ForeignKey(
        authlib.get_user_model(),
        unique=True,
        on_delete=models.CASCADE,
    )

class eduDonationReq(models.Model):
    currenteduOpts=(
        ('none','none'),
        ('pri','Primary School'),
        ('hi','High School'),
        ('bach','Bachelor\'s Degree'),
        ('mas','Master\'s Degree')
    )
    seekingeduOpts = (
        ('pri', 'Primary School'),
        ('hi', 'High School'),
        ('bach', 'Bachelor\'s Degree'),
        ('mas', 'Master\'s Degree')
    )
    firstname = models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone_number = models.DecimalField(max_digits=10, decimal_places=0)
    currentedu=models.CharField(max_length=50,choices=currenteduOpts)
    seekingedu=models.CharField(max_length=50,choices=seekingeduOpts)
    reqamt=models.DecimalField(max_digits=7,decimal_places=0)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    note=models.TextField(max_length=1000,null=True,blank=True)

class OrganDonors(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    bloodgroups = (
    ('O+ve', 'O+ve'), ('O-ve', 'O-ve'), ('A+ve', 'A+ve'), ('A-ve', 'A-ve'), ('B+ve', 'B+ve'), ('B-ve', 'B-ve'),
    ('AB+ve', 'AB+ve'), ('AB-ve', 'AB-ve'))
    bloodgroup = models.CharField(max_length=5, choices=bloodgroups)
    gender=(('Male','Male'),('Female','Female'),('Prefer not to say','Prefer not to say'))
    Gender=models.CharField(max_length=50, choices=gender)
    days = ((str(i),str(i)) for i in range(1,31))
    years = ((str(i),str(i)) for i in range(1947,2019))
    Year = models.CharField(max_length=4, choices=years)
    Months = (
    ("1", "Jan"), ("2", "Feb"), ("3", "Mar"), ("4", "Apr"), ("5", "May"), ("6", 'Jun'), ("7", "Jul"), ("8", "Aug"),
    ("9", "Sep"), ("10", "Oct"),
    ("11", "Nov"), ("12", "Dec"))
    Month = models.CharField(max_length=3, choices=Months)
    Day = models.CharField(max_length=2, choices=days)
    Address=models.CharField(max_length=100)
    Phone_number=models.DecimalField(max_digits=10,decimal_places=0)
    Email=models.EmailField()
    Religions=(("Hindu","Hindu"),("Christian","Christian"),("Muslim","Muslim"),("Buddhist","Buddhist"),("Sikh","Sikh"))
    Religion=models.CharField(max_length=50,choices=Religions)
    Parts_you_want_to_donate=(("Heart","Heart"),("Lungs","Lungs"),("Kidneys","Kidneys"),("Liver","Liver"),("Corneas","Corneas"),("Pancreas","Pancreas")
            ,("Tissue","Tissue"),("Small bowel","Small bowel"))
    Parts_you_want_to_donate=MultiSelectField(choices=Parts_you_want_to_donate)

class Fundraisers(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    purposeopts=(('medical','Medical'),('business','Business'),('personal','Personal'))
    Purpose=models.CharField(max_length=50,choices=purposeopts)
    amount=models.PositiveIntegerField()
    gender=(('Male','Male'),('Female','Female'),('Prefer not to say','Prefer not to say'))
    Gender=models.CharField(max_length=50, choices=gender)
    days = ((str(i),str(i)) for i in range(1,31))
    years = ((str(i),str(i)) for i in range(1947,2019))
    Year = models.CharField(max_length=4, choices=years)
    Months = (
    ("1", "Jan"), ("2", "Feb"), ("3", "Mar"), ("4", "Apr"), ("5", "May"), ("6", 'Jun'), ("7", "Jul"), ("8", "Aug"),
    ("9", "Sep"), ("10", "Oct"),
    ("11", "Nov"), ("12", "Dec"))
    Month = models.CharField(max_length=3, choices=Months)
    Day = models.CharField(max_length=2, choices=days)
    Phone_number=models.DecimalField(max_digits=10,decimal_places=0)
    Email=models.EmailField()
    Address=models.CharField(max_length=100)
    verification=models.BooleanField(default=False)

