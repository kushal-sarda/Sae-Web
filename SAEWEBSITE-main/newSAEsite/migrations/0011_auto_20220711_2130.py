# Generated by Django 3.2.6 on 2022-07-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newSAEsite', '0010_auto_20220711_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('post_order',)},
        ),
        migrations.AddField(
            model_name='profile',
            name='post_order',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')], default='20'),
        ),
    ]
