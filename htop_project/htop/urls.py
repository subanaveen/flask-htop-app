from django.urls import path
from . import views
from htop.views import home


urlpatterns = [
    path('', home, name='home'),
    path('htop/', views.htop, name='htop'),
    path('admin/', admin.site.urls),  # Keep your other URLs here
]
