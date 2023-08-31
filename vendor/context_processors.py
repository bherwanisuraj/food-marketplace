from .models import Vendor

def get_vendor(request):
    vendor = Vendor.objects.get(vendor=request.user)
    return dict(vendor=vendor)