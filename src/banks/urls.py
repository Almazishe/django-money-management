from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('new/', views.create_bank, name='create-bank'),    
]
