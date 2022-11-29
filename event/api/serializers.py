from rest_framework import serializers

from event.models import Event

# Create serializers

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('created_at', 'modified_at')

    def to_representation(self, instance):
        representation = super(EventListSerializer, self).to_representation(instance)
        representation['clean_date'] = instance.date.strftime('%b %d, %Y - %H:%M:%S UTC')
        representation['date'] = instance.date.strftime('%Y-%m-%dT%H:%M')
        return representation

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
