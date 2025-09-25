from django.urls import path
from . import views

urlpatterns = [
    path('', views.Columnviews, name='column'),
]