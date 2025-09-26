from django.urls import path
from . import views

urlpatterns = [
    path('', views.Webinarviews, name='webinar'),
]