from django.db import models
from django_countries.fields import CountryField

from core.models import AbstractCustomModel

# Create your models here.

class Event(AbstractCustomModel):
    name = models.CharField(max_length=100)
    location = CountryField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-id']
