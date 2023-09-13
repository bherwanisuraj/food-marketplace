from django.urls import path, include
from . import views
from accounts.views import myAccount

urlpatterns = [
    path('', myAccount, name='my-account'),
    path('vendor-dashboard/', views.vendorDashboard, name='vendor-dashboard'),
    path('my-restaurant/', views.myRestaurant, name = 'my-restaurant'),
    path('menu-builder/', views.menuBuilder, name='menu-builder'),
]