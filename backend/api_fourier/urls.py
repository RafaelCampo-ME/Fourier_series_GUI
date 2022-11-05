from django.urls import path
from .views import DocuAPIViewf 

urlpatterns = [
    path('',DocuAPIViewf.as_view()),
    path('lista',DocuAPIViewf.fourierList)
    ]