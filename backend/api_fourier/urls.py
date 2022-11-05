from django.urls import path
from .views import documentationAPIviews


urlpatterns = [
    path('', documentationAPIviews.as_view()),
]