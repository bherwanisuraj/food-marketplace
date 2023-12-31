from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .models import Vendor
from accounts.models import UserProfile
from accounts.forms import VendorForm
from .forms import VendorProfileForm
from django.contrib import messages
from menu.models import Category

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
    vendor_instance = get_object_or_404(Vendor, vendor=request.user)
    user_profile = get_object_or_404(UserProfile, user = request.user)

    if request.method == "POST":
        profile_form = VendorProfileForm(request.POST, request.FILES, instance=user_profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=vendor_instance)
        if profile_form.is_valid() and vendor_form.is_valid():
            vendor_form.save()
            profile_form.save()
            messages.success(request, "Restaurant Updated!")
            return redirect('my-restaurant')
        else:
            pass

    else:    
        profile_form = VendorProfileForm(instance=user_profile)
        vendor_form = VendorForm(instance=vendor_instance)
    context = {
        'vendorform': vendor_form,
        'profileform': profile_form,
        # 'userprofile': user_profile,
        # 'vendorinstance': vendor_instance,
    }
    return render(request, 'vendor/my-restaurant.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def menuBuilder(request):
    vendor = Vendor.objects.get(vendor=request.user)
    categories = Category.objects.filter(vendor=vendor)
    context = {
        'categories' : categories,
    }
    return render(request, 'vendor/menu-builder.html', context)
