# Generated by Django 4.2.4 on 2023-09-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_category_options_alter_fooditem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='desciption',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
