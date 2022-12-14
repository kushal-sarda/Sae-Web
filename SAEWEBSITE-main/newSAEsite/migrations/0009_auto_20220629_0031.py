# Generated by Django 3.2.6 on 2022-06-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newSAEsite', '0008_alter_profile_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baja',
            options={'ordering': ('-batch',)},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('-batch',)},
        ),
        migrations.AddField(
            model_name='baja',
            name='batch',
            field=models.IntegerField(choices=[(2023, '2023'), (2024, '2024'), (2025, '2025')], default=2023),
        ),
    ]
