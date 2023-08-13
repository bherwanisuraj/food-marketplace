from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'role')
    ordering = ('-date_joined',)
    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()
    

# class CustomUserProfileAdmin(UserAdmin):
#     list_display = ('user', 'city', 'state', 'country', 'modified_at')
#     fieldsets = ()
#     filter_horizontal = ()
#     list_filter = ()


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
