from django.shortcuts import render
from api_fourier.models import documentation

##from rest_framework import generics
#from api_fourier.models import documentation
##from  import BookSerializer



# Create your views here.
class documentationAPIView():
    queryset = documentation.objects.all() 
    