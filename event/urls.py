from django.urls import include, path

from . import views

app_name = 'event'

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),

    # Backend Endpoints
    path('api/', include('event.api.urls', namespace='event-api')),
]
