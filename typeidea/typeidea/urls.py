from django.contrib import admin
from django.urls import path, include
from .custom_site import custom_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cus_admin/', custom_site.urls),
    path('blog/', include('blog.urls')),
    path('config/', include('config.urls')),
]
