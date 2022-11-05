from django.urls import path

from .views import documentationAPIView 

#urlpatterns = [
#    path('', documentationAPIView.as_view())
#]

urlpatterns = [
    path('about/', documentationAPIView.as_view(template_name="about.html")),
]