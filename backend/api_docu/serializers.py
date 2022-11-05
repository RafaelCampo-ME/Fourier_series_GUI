from rest_framework import serializers
from api_fourier.models import documentation

#A serializer transalates data into a json format and is diaplayed at an API endpoint

class docuSerializer(serializers.ModelSerializer):
    class Meta:
        model = documentation
        fields = ("created_at", "updated_at", "author", "title", "body" )