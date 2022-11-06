from rest_framework import serializers
from api_fourier.models import documentation
##from ...FourierLogic.fourier_data import 


class docuSerializer(serializers.ModelSerializer):
    class Meta:
        model = documentation
        fields = ("created_at", "updated_at", "author", "title", "body" )
