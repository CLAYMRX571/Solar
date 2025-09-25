from django.urls import path
from . import views

urlpatterns = [
    path('', views.Advanceviews, name='advance'),
]