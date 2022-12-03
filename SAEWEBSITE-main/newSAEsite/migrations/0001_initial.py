# Generated by Django 3.2.5 on 2021-08-11 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import newSAEsite.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True)),
                ('location', models.CharField(choices=[('online', 'ONLINE'), ('offline', 'OFFLINE')], default='online', max_length=200)),
                ('poster', models.ImageField(null=True, upload_to='event_poster')),
                ('Writeup', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('post', models.CharField(choices=[('PRESIDENT', 'President'), ('VICE PRESIDENT', 'Vice President'), ('GENERAL SECRETARY', 'General Secretary'), ('TREASURER', 'Treasurer'), ('CONVENER', 'Convener'), ('TECH HEAD', 'Tech Head'), ('DESIGN HEAD', 'Design Head'), ('WEBD', 'web D'), ('PUBLIC RELATIONS HEAD', 'Public relations Head'), ('CREATIVE HEAD', 'Creative Head'), ('SPONSORSHIP HEAD', 'Sponsorship Head'), ('ACCOMODATION,TRAVEL AND HOSPITALITY HEAD', 'Accomodation,travel and Hospitality Head'), ('OPERATIONS HEAD', 'Operations Head'), ('BAJA COORDINATOR', 'Baja coordinator'), ('WORKSHOP HEAD', 'Workshop Head'), ('EVENTS HEAD', 'Events Head'), ('EVENTS AND FEST COORDINATOR', 'Events and Fest coordinator'), ('LOGISTIC HEAD', 'Logistic Head'), ('NONE', 'None')], default='None', max_length=40)),
                ('graduation_year', models.IntegerField(choices=[(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Final Year')], default=2)),
                ('department', models.CharField(choices=[('MANAGEMENT', 'Management'), ('TECHNICAL', 'Technical'), ('WEBD', 'Web Developement'), ('GRAPHICS', 'Graphics and Photography'), ('NDORS', 'NDORS')], default='FIRST', max_length=20)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(null=True, upload_to='profile_pics', validators=[newSAEsite.models.validate_image_size])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-graduation_year',),
            },
        ),
    ]