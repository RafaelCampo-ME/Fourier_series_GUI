from django.urls import path
from .views import DocuAPIView 

urlpatterns = [
    path('',DocuAPIView.as_view()),
    ]