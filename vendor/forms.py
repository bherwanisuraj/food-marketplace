from .models import Vendor
from django import forms
from accounts.models import UserProfile

def VendroProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ("profile_picture", "cover_picture", "address_line_1")