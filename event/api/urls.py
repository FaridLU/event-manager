from django.urls import include, path

from . import views

app_name = 'event'

urlpatterns = [
    path('events/', views.EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:id>', views.EventReadUpdateDeleteAPIView.as_view(), name='event-read-update-delete'),
]
