from rest_framework import generics
from api_fourier.models import documentation
from .serializers import docuSerializer

class  DocuAPIView(generics.ListAPIView):
    queryset = documentation.objects.all()
    serializer_class = docuSerializer