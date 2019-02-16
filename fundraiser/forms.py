from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from fundraiser.models import BloodDonors,eduDonors,eduDonationReq,OrganDonors,Fundraisers

class bloodDonorForm(forms.ModelForm):
    class Meta:
        model=BloodDonors
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class eduHelpForm(forms.ModelForm):
    class Meta:
        model=eduDonationReq
        fields='__all__'
        labels={
            'firstname':'First Name',
            'lastname':'Last Name',
            'phone_number':'Contact number',
            'currentedu':'Highest Education till now',
            'seekingedu':'Seeking loan for',
            'reqamt':'Fees'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['placeholder']='Optional'

class eduDonorForm(forms.ModelForm):
    class Meta:
        model=eduDonors
        fields='__all__'
        labels={
            'notification':'Enable this to get notified about requests'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name!='notification':
                field.widget.attrs['class'] = 'form-control'

class OrganDonorForm(forms.ModelForm):
    class Meta:
        model=OrganDonors
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name=='Day' or field_name=='Year' or field_name=='Month':
                field.widget.attrs['class']='form-control checkclass'
            elif field_name != 'Parts_you_want_to_donate':
                field.widget.attrs['class'] = 'form-control'

class NewFundRaiserForm(forms.ModelForm):
    class Meta:
        model=Fundraisers
        exclude=('verification',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class userSignupForm(UserCreationForm):
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=30)
        email = forms.EmailField(max_length=254)
        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                    field.widget.attrs['class'] = 'form-control'

class userloginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields='__all__'


