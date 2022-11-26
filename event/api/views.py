from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.exception_handler import get_error_response
from core.utils.generic_pagination import get_paginated_data
from event.models import Event

from .serializers import (BasicEventSerializer, EventCreateUpdateSerializer,
                          EventListSerializer, EventSerializer)


class EventListCreateAPIView(APIView):
    # List of events
    def get(self, request) -> Response:
        try:
            instance = Event.objects.all()

            # Paginate data
            paginated_data = get_paginated_data(Event, instance, request)
            paginated_instances = paginated_data.pop('paginated_instances')

            serializer = EventListSerializer(paginated_instances, many=True)

            data = {
                'data': serializer.data,
                **paginated_data,
            }
            return Response({'status': 'success', 'data': data}, status=status.HTTP_200_OK)
        except Exception as e:
            return get_error_response(e)

    # Create event
    def post(self, request) -> Response:
        try:
            serializer = EventCreateUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()

            return Response(
                {'status': 'success', 'message': 'Event is Created Successfully.', 'data': {'id': instance.id}},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return get_error_response(e)


class EventReadUpdateDeleteAPIView(APIView):
    # Read an event
    def get(self, request, id) -> Response:
        try:
            instance = Event.objects.get(id=id)
            serializer = EventSerializer(instance)

            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return get_error_response(e)
    
    # Update an event
    def put(self, request, id) -> Response:
        try:
            instance = Event.objects.get(id=id)

            serializer = EventCreateUpdateSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({'status': 'success', 'message': 'Event is updated successfully.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return get_error_response(e)

    # Delete an event
    def delete(self, request, id):
        try:
            Event.objects.get(id=id).delete()
            return Response({'status': 'success', 'message': 'Event is deleted successfully.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return get_error_response(e)
