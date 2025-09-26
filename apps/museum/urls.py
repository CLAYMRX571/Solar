from django.urls import path
from . import views

urlpatterns = [
    path('', views.Museumviews, name='museum'),
]