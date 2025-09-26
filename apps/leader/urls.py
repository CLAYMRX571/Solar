from django.urls import path
from . import views

urlpatterns = [
    path('', views.Leaderviews, name='leader'),
]