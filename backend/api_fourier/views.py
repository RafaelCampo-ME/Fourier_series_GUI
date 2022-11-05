from rest_framework import generics
from api_fourier.models import documentation
from .serializer import docuSerializer

class  DocuAPIViewf(generics.ListAPIView):
    queryset = documentation.objects.filter(title="About Fourier Series GUI project") 
    serializer_class = docuSerializer
