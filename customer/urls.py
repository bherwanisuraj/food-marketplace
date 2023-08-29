from django.urls import path, include
from . import views
from accounts.views import myAccount

urlpatterns = [
    path('', myAccount, name='my-account'),
    path('customer-dashboard/', views.customerDashboard, name='customer-dashboard'),
]