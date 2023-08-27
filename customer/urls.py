from django.urls import path, include
from . import views

urlpatterns = [
    path('customer-dashboard/', views.customerDashboard, name='customer-dashboard'),
]