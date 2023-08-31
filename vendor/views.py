from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .models import Vendor


def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendorDashboard(request):
    # vendor = Vendor.objects.get(vendor=request.user)
    # context = {
    #     'vendor':vendor,
    # }
    return render(request, 'vendor/vendor-dashboard.html')

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def myRestaurant(request):
    return render(request, 'vendor/my-restaurant.html')


