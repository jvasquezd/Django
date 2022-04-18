from django.urls import path, include
from core.dps.views import *

app_name='dps'

urlpatterns = [
    path('uno/',myfirstview),
]