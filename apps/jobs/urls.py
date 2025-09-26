from django.urls import path
from . import views

urlpatterns = [
    path('', views.Jobsviews, name='jobs'),
]