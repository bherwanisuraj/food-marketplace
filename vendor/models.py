from django.db import models
from .validators import pdfValidator
from accounts.models import User, UserProfile
from accounts.utils import sendMail


class Vendor(models.Model):
    vendor = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=50)
    vendor_license = models.FileField(upload_to='vendor/license', validators=[pdfValidator])
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name
    

    def save(self, *agrs, **kwargs):
        if self.pk is not None:
            vendor = Vendor.objects.get(pk = self.pk)
            if vendor.is_approved != self.is_approved:
                if self.is_approved is True:
                    sendMail(None, self.vendor, "Congratulation! Your Restaurant has been approved.", "vendor-approval", False, self.is_approved)
                else:
                    sendMail(None, self.vendor, "We're Sorry! Your Restaurant application was declined.", "vendor-approval", False, self.is_approved)

        return super(Vendor, self).save(**kwargs)
