from django.contrib import admin
from core.dps.models import Patient, BDI, Sack
# Register your models here.
admin.site.register(Patient)
admin.site.register(BDI)
admin.site.register(Sack)
