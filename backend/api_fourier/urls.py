from django.urls import path
from .views import pyfourierDataAPI 

urlpatterns = [
    path('',pyfourierDataAPI.fourierList),
    path('data',pyfourierDataAPI.fourierAprox)
    ]