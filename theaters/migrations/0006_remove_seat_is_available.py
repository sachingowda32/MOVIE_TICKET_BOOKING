# Generated by Django 5.2.2 on 2025-06-27 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theaters', '0005_seat_is_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='is_available',
        ),
    ]
