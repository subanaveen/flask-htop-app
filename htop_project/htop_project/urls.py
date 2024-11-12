from django.contrib import admin
from django.urls import path
from htop import views  # Import the views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),  # Map the home view to the root URL
]
