from django.shortcuts import render, redirect
from .forms import UserForm, VendorForm
from .models import User, UserProfile
from django.contrib import messages, auth
from .utils import detectUser, uidAndTokenChecker
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .utils import sendMail

from django.contrib.auth.tokens import default_token_generator



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
            sendMail(request, user, "Please click on the below link to activate your account.", "account-verification-email", True, False)
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
            sendMail(request, user, "Please click on the below link to activate your account.", "account-verification-email", True, False)
            messages.success(request, 'Your restaurant has been created.')

    else:
        form = UserForm()
        vendor_form = VendorForm()

    context = {
        'form': form,
        'vendor_form': vendor_form,
    }

    return render(request, 'accounts/register-vendor.html', context)

def activate(request, uidb64, token):

    user, uid = uidAndTokenChecker(uidb64)    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Congrats! Your account is activated. You can login now.")
        return redirect('my-account')

    else:
        messages.error('Invalid Link. Please try again.')
        return redirect('my-account')


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


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            sendMail(request, user, "Please click on the below link to reset your password", "password-reset-mail", True, False)
            messages.success(request, 'Password reset link has been sent to your email address.')

        else:
            messages.error(request, 'Account associated with the email address does not exist.')

    return render(request, 'accounts/forgot-password.html')

def resetPasswordValidate(request, uidb64, token):
    user, uid = uidAndTokenChecker(uidb64)
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'Please reset your password')
        return redirect('reset-password')
    
    else:
        messages.error(request, 'Link is expired.')
        return redirect('login')
    
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password request successful.')
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match. Enter it again.")
            return redirect('reset-password')
    return render(request, 'accounts/reset-password.html')