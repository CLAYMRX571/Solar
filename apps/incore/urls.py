from django.urls import path
from . import views

urlpatterns = [
    path('', views.Incoreviews, name='incore'),
]