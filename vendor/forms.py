from .models import Vendor
from django import forms
from accounts.models import UserProfile

class VendorProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ["profile_picture", "cover_picture", "address_line_1", "address_line_2", "city", "state", "country", "pincode", "longitude", "latitude"]