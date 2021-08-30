#every app in your project should have their url
from django.urls import path

from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), # For our-domain.com/meetups, this should beome active
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]