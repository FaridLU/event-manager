from rest_framework import serializers

from event.models import Event

# Create serializers

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('created_at', 'modified_at')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('created_at', 'modified_at')


class BasicEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('created_at', 'modified_at')
