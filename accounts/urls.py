from django.urls import path, include
from . import views

urlpatterns = [
    path('register-user/', views.registerUser, name='register-user'),
]
