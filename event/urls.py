from django.urls import include, path

app_name = 'event'

urlpatterns = [
    path('api/', include('event.api.urls')),
]
