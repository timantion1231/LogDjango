from django.urls import path, include
from django.contrib.auth import urls

urlpatterns = [
    path('', include('django.contrib.auth.urls'))
]