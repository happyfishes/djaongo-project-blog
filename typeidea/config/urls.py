from django.urls import path
from config.views import *

urlpatterns = [
    path('link/', link),
]
