# Generated by Django 3.1.7 on 2021-04-04 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mechanics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mechanic',
            old_name='primary_car_make',
            new_name='primary_car_brand',
        ),
    ]
