from django.urls import path, include
from .views import main,api
urlpatterns = [
    path('',main,name='main'),
    path('api/',api,name='api'),
]