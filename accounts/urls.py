"""URL configuration for user authentication and registration system."""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Home page
    path('', include('django.contrib.auth.urls'))
]