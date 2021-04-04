from django.contrib import admin
from django.urls import path
from .custom_site import custom_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('super_admin/', admin.site.urls),
    path('cus_admin/', custom_site.urls),
]
