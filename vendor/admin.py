from django.contrib import admin
from vendor.models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'is_approved', 'created_at')
    list_display_links = ('vendor',)

admin.site.register(Vendor, VendorAdmin)
