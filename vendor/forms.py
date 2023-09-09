from .models import Vendor
from django import forms
from accounts.models import UserProfile

class VendorProfileForm(forms.ModelForm):   
    # latitude = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # longitude = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))


    class Meta:
        model = UserProfile
        fields = ["profile_picture", "cover_picture", "address", "city", "state", "country", "pincode", "longitude", "latitude"]

    def __init__(self, *args, **kwargs):
        super(VendorProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'longitude' or field == 'latitude':
                self.fields[field].widget.attrs['readonly'] = 'readonly'

            elif field == 'address':
                self.fields[field].widget.attrs['placeholder'] = 'Start typing...'