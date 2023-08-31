from .models import Vendor

def get_vendor(request):
    try:
        vendor = Vendor.objects.get(vendor=request.user)
        
    except:
        vendor = None
    
    return dict(vendor=vendor)