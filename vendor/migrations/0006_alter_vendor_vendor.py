# Generated by Django 4.2.4 on 2023-08-30 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0005_alter_vendor_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
