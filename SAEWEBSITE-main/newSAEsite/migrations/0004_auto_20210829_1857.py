# Generated by Django 3.2.6 on 2021-08-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newSAEsite', '0003_alter_event_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]