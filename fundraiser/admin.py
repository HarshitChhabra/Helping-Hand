from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.BloodDonors)
admin.site.register(models.eduDonationReq)
admin.site.register(models.eduDonors)
admin.site.register(models.OrganDonors)
admin.site.register(models.Fundraisers)