# Generated by Django 4.2.4 on 2023-09-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
