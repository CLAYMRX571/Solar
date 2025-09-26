from django.urls import path
from . import views

urlpatterns = [
    path('', views.Youngviews, name='young'),
]