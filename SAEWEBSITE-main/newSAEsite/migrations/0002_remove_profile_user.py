# Generated by Django 3.2.5 on 2021-08-11 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newSAEsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
