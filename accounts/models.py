from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    
    def create_user(self, first_name, last_name, username, email, password=None):

        if not email:
            raise ValueError('Email is required')
        
        if not username:
            raise ValueError('Username is required')
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)

        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
        )

        user.is_staff = True
        user.is_superadmin = True
        user.is_admin = True
        user.is_active = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    CUSTOMER = 0
    RESTAURANT = 0

    ROLES = (
        (CUSTOMER, 'Customer'),
        (RESTAURANT, 'Restaurant'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=12, unique=True, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLES, blank=True, null=True)

    #required fields
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_picture', blank=True, null=True)
    cover_picture = models.ImageField(upload_to='users/cover_pictures', blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    pincode = models.CharField(max_length=5, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
        