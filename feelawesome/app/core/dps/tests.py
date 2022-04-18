from django.test import TestCase
from config.wsgi import *
from core.dps.models import *
# Create your tests here.

#listar your
query = Patient.objects.all()
print(query)

#Insert your tests here
p=Patient()
p.age=19
p.type_family='Nuclear'
p.save()

#Ediciom
try:
    q = Patient.objects.get(id=1)
    print(q)
except Exception as e:
    print(e)

#Eliminacion
r = Patient.objects.get(id=1)
r.delete()

#Listar por filtrov

m=Patient.objects.filter(tfamily__icontains='nuclear')

for i in m:
    print(i.tfamily)