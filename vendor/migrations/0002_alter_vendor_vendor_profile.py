# Generated by Django 4.2.4 on 2023-08-18 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_role'),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_profile', to='accounts.userprofile'),
        ),
    ]
