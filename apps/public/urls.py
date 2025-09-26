from django.urls import path
from . import views

urlpatterns = [
    path('', views.Publicviews, name='public'),
]