# Generated by Django 4.2.3 on 2023-10-26 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superadmin',
        ),
    ]
