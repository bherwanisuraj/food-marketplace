from django.urls import path, include
from . import views

urlpatterns = [
    path('register-user/', views.registerUser, name='register-user'),
    path('register-vendor/', views.registerVendor, name='register-vendor'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('customer-dashboard/', views.customerDashboard, name='customer-dashboard'),
    path('vendor-dashboard/', views.vendorDashboard, name='vendor-dashboard'),
    path('my-account/', views.myAccount, name='my-account'),
]
