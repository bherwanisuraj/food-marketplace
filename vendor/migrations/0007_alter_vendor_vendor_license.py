# Generated by Django 4.2.4 on 2023-09-08 10:36

from django.db import migrations, models
import vendor.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_alter_vendor_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_license',
            field=models.FileField(upload_to='vendor/license', validators=[vendor.validators.pdfValidator]),
        ),
    ]