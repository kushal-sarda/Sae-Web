from rest_framework import serializers
from newSAEsite.models import Profile, Event, Baja


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'post', 'post_order','graduation_year', 'department', 'linkedin','facebook','insta' ,'email', 'image','batch')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'date', 'location', 'poster', 'Writeup')

class BajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baja
        fields = ('name', 'image','batch' ,'post','linkedin','facebook','insta')
