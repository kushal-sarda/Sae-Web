# Generated by Django 3.2.6 on 2022-07-11 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newSAEsite', '0009_auto_20220629_0031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baja',
            options={'ordering': ('batch',)},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('batch', 'post')},
        ),
    ]
