from django.urls import path, include
from . import views

urlpatterns = [
    path('vendor-dashboard/', views.vendorDashboard, name='vendor-dashboard'),
]