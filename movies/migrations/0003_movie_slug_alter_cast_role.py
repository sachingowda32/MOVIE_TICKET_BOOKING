# Generated by Django 5.2.2 on 2025-06-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='role',
            field=models.CharField(blank=True, choices=[('Hero', 'Hero'), ('Heroine', 'Heroine'), ('Supporting Actor', 'Supporting Actor'), ('Villain', 'Villain')], max_length=100, null=True),
        ),
    ]
