# Generated by Django 4.2.3 on 2023-10-27 06:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_contents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
