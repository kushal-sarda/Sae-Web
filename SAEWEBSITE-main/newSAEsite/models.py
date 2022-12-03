from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
import datetime


def validate_image_size(value):
    limit = 1 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 1 MiB.')

def profile_pics(instance, filename):
    return 'pics/{filename}'.format(filename=filename)

class Profile(models.Model):
    yr_choices = [
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Final Year'),
    ]
    dept_choices = [
        # ('OFFICE BEARERS','Office Bearers'),
        ('MANAGEMENT', 'Management'),
        ('MANAGEMENT AND CONTENT WRITING', 'Management-Content'),
        ('TECHNICAL-ROBOTICS', 'Technical-Robotics'),
        ('TECHNICAL-AUTOMOBILE', 'Technical-Automobile'),
        ('WEB DEVELOPMENT', 'WebD'),
        ('GRAPHICS DESIGNING AND VIDEOGRAPHY', 'Graphics'),
        ('NDORS', 'NDORS'),
    ]
    post_choices = [
        ('PRESIDENT', 'President'),
        ('VICE PRESIDENT', 'Vice President'),
        ('GENERAL SECRETARY', 'General Secretary'),
        ('TREASURER', 'Treasurer'),
        ('CONVENER', 'Convener'),
        ('TECH HEAD', 'Tech Head'),
        ('DESIGN HEAD', 'Design Head'),
        ('WEBD HEAD', 'webD Head'),
        ('PUBLIC RELATIONS HEAD', 'Public relations Head'),
        ('CREATIVE HEAD', 'Creative Head'),
        ('SPONSORSHIP HEAD', 'Sponsorship Head'),
        ('ACCOMODATION,TRAVEL AND HOSPITALITY HEAD', 'Accomodation,travel and Hospitality Head'),
        ('CORPORATE COMMUNICATION HEAD', 'Head of Corporate Communication'),
        ('OPERATIONS HEAD', 'Operations Head'),
        ('BAJA COORDINATOR', 'Baja coordinator'),
        ('WORKSHOP HEAD', 'Workshop Head'),
        ('EVENTS HEAD', 'Events Head'),
        ('EVENTS AND FEST COORDINATOR', 'Events and Fest coordinator'),
        ('LOGISTIC HEAD', 'Logistic Head'),
        ('Co CONVENOR','Co convenor'),
        ('ASSISTANT GENERAL SECRETARY','Assistant General Secretary'),
        ('AUTOMOBILE HEAD','Automobile head'),
        ('NONE', 'None'),
    ]

    BATCH_CHOICES = [
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
    ]
    
    Order_choices = [
        (1,'President'),
        (2, 'General Secretary'),       
        (3, 'Treasurer'),   
        (4, 'Vice President'),      
        (5,'Assistant General Secretary'),  
        (6,'Convener'),
        (7,'Co convenor'),  
        (8, 'Head of Corporate Communication'),    
        (9, 'Operations Head'), 
        (10, 'Tech Head'), 
        (11, 'Logistic Head'), 
        (12, 'webD Head'), 
        (13,'Automobile head'),                  
        (14, 'Baja coordinator'),   
        (15, 'Design Head'),                 
        (16, 'Public relations Head'),
        (17, 'Accomodation,travel and Hospitality Head'),   
        (18, 'Events Head'), 
        (19, 'Workshop Head'), 
        (20, 'None'),
    ]
    

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50)
    post = models.CharField(max_length=40, choices=post_choices, default='None')
    post_order=models.IntegerField(choices=Order_choices,default='None')
    graduation_year = models.IntegerField(choices=yr_choices, default=2)
    department = models.CharField(max_length=120, choices=dept_choices, default='FIRST')
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    insta = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(null=True, blank=False, upload_to='profile_pics', validators=[validate_image_size])
    batch = models.IntegerField(choices=BATCH_CHOICES, default=2023)

    class Meta:
        ordering = ('post_order','batch','first_name',)

    def __str__(self):
        return (self.first_name + self.last_name)
        # return str(self.user)

    def isPostHolder(self):
        if self.post == 'NONE':
            return 0
        else:
            return 1

def event_poster(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    location = models.CharField(max_length=200)
    poster = models.ImageField(null=True, blank=False, upload_to='event_poster', height_field=None, width_field=None)
    Writeup = models.TextField()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return str(self.name)

def baja_pics(instance, filename):
    return 'bajas/{filename}'.format(filename=filename)

class Baja(models.Model):
    
    BATCH_CHOICES = [
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
    ]
    
    
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=False, upload_to='baja_pics', validators=[validate_image_size])
    batch = models.IntegerField(choices=BATCH_CHOICES, default=2023)
    post = models.CharField(max_length=100)
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    insta = models.URLField(null=True, blank=True)
    
    class Meta:
        ordering = ('batch',)
    def __str__(self):
        return str(self.name)
