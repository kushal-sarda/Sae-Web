# Generated by Django 3.2.6 on 2022-07-26 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newSAEsite', '0013_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('post_order', 'batch')},
        ),
    ]
