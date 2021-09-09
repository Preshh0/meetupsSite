#every app in your project should have their url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='all-meetups'), # For our-domain.com/meetups, this should beome active
    path('<slug:meetup_slug>/success', views.confirm_registration, name="confirm-registration"),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),
]