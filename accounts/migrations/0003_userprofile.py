# Generated by Django 4.2.4 on 2023-08-13 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/profile_picture')),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to='users/cover_pictures')),
                ('address_line_1', models.CharField(blank=True, max_length=50, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('pincode', models.CharField(blank=True, max_length=5, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
