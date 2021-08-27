#every app in your project should have their url
from django.urls import path

from . import views

urlpatterns = [
    path('meetups/', views.index) # For our-domain.com/meetups, this should beome active
]