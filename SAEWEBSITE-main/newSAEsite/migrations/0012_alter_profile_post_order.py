# Generated by Django 3.2.6 on 2022-07-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newSAEsite', '0011_auto_20220711_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='post_order',
            field=models.IntegerField(choices=[(1, 'President'), (2, 'Vice President'), (3, 'Treasurer'), (4, 'General Secretary'), (5, 'Assistant General Secretary'), (6, 'Convener'), (7, 'Co convenor'), (8, 'Head of Corporate Communication'), (9, 'Operations Head'), (10, 'Tech Head'), (11, 'Logistic Head'), (12, 'webD Head'), (13, 'Automobile head'), (14, 'Baja coordinator'), (15, 'Design Head'), (16, 'Public relations Head'), (17, 'Accomodation,travel and Hospitality Head'), (18, 'Events Head'), (19, 'Workshop Head'), (20, 'None')], default='None'),
        ),
    ]
