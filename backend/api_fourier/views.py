from rest_framework import generics
from api_fourier.models import documentation
from .serializer import docuSerializer
from django.http import JsonResponse 

class  DocuAPIViewf(generics.ListAPIView):
    queryset = documentation.objects.filter(title="About Fourier Series GUI project") 
    serializer_class = docuSerializer

    def fourierList(request,*args,**kwargs):
        lista = [1,2,3,4]
        return JsonResponse({"list":lista})