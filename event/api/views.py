from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.exception_handler import (get_error_response,
                                          get_success_response)
from core.utils.generic_pagination import get_paginated_data
from event.models import Event

from .serializers import (BasicEventSerializer, EventCreateUpdateSerializer,
                          EventListSerializer, EventSerializer)


class EventListCreateAPIView(APIView):
    # List of events
    def get_queryset(self):
        return Event.objects.all()

    def get(self, request) -> Response:
        try:
            qs = self.get_queryset()
            records_total = qs.count()
            records_filtered = qs.count()

            draw = request.GET.get('draw')

            # Paginate data
            paginated_data = get_paginated_data(Event, qs, request)
            paginated_instances = paginated_data.pop('paginated_instances')

            # Serialize results
            serializer = EventListSerializer(paginated_instances, many=True)
            response = {
                'draw': draw,
                'recordsTotal': records_total,
                'recordsFiltered': records_filtered,
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return get_error_response(e)

    # Create event
    def post(self, request) -> Response:
        try:
            serializer = EventCreateUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()

            return get_success_response(message='Event is Created Successfully.')

        except Exception as e:
            return get_error_response(e)


class EventReadUpdateDeleteAPIView(APIView):

    # Read an event
    def get(self, request, id) -> Response:
        try:
            instance = Event.objects.get(id=id)
            serializer = EventSerializer(instance)

            return get_success_response(data=serializer.data)

        except Exception as e:
            return get_error_response(e)
    
    # Update an event
    def put(self, request, id) -> Response:
        try:
            instance = Event.objects.get(id=id)

            serializer = EventCreateUpdateSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return get_success_response(message='Event is updated successfully.')

        except Exception as e:
            return get_error_response(e)

    # Delete an event
    def delete(self, request, id):
        try:
            Event.objects.get(id=id).delete()
            return get_success_response(message='Event is deleted successfully.')

        except Exception as e:
            return get_error_response(e)
