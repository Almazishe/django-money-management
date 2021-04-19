from django.urls import path

from . import views


urlpatterns = [
    path('operations/new/', views.create_operation, name='create-operation')
]
