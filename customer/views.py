from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from accounts.models import UserProfile


def check_role_customer(user):
    if user.role == 0:
        return True
    else:
        raise PermissionDenied

@login_required(login_url='login')
@user_passes_test(check_role_customer)
def customerDashboard(request):
    customer = UserProfile.objects.get(user=request.user)
    context = {
        'customer': customer,
    }
    return render(request, 'customer/customer-dashboard.html', context)