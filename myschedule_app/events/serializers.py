# import the serializers module from the rest_framework package
from rest_framework import serializers
# import the Event model
from .models import Event

class EventsSerializer(serializers.ModelSerializer):
    '''Serializer for the Event model'''
    class Meta:
        '''Meta class for the Event model'''
        model = Event
        # all fields to be serialized and deserialized
        fields = '__all__'