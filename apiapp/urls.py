# apiapp/urls.py
from django.urls import path
from .views import fetch_api_data, index

urlpatterns = [
    path('', index, name='index'),
    path('fetch/', fetch_api_data, name='fetch_api_data'),
]