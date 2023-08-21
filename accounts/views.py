from django.shortcuts import render, redirect
from .forms import UserForm, VendorForm
from .models import User, UserProfile
from django.contrib import messages, auth
from .utils import detectUser
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

def check_role_customer(user):
    if user.role == 0:
        return True
    else:
        raise PermissionDenied
    
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied

def registerUser(request):

    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged-in')
        return redirect('dashboard')

    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.phone = phone
            user.save()
            messages.success(request, 'Congratulations! Your account has been registered.')
            return redirect('register-user')        
    else:
        form = UserForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register-user.html', context)

def registerVendor(request):

    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged-in')
        return redirect('dashboard')

    elif request.method == 'POST':
        form = UserForm(request.POST)
        vendor_form = VendorForm(request.POST, request.FILES)

        if form.is_valid() and vendor_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.RESTAURANT
            user.phone = phone
            user.save()
            vendor = vendor_form.save(commit=False)
            vendor.vendor = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, 'Your restaurant has been created.')

    else:
        form = UserForm()
        vendor_form = VendorForm()

    context = {
        'form': form,
        'vendor_form': vendor_form,
    }

    return render(request, 'accounts/register-vendor.html', context)


def login(request):

    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged-in')
        return redirect('my-account')

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email = email, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Succesfull!')
            return redirect('my-account')

        else:
            messages.error(request, 'Invalid credentials')

    else:
        print("error")

    return render(request, 'accounts/user-login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.info(request, 'You are not logged out')
    return render(request, 'accounts/user-login.html')

@login_required(login_url='login')
def myAccount(request):
    user = request.user
    url = detectUser(user)
    
    return redirect(url)


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def customerDashboard(request):    
    return render(request, 'accounts/customer-dashboard.html')


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendorDashboard(request):    
    return render(request, 'accounts/vendor-dashboard.html')