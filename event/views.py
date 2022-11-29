import json

from django.shortcuts import render
from django.views.generic import TemplateView

from .data import COUNTRIES

# Create your views here.

class DashboardView(TemplateView):
    template_name = 'event/event_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['countries'] = COUNTRIES

        # NOTE: The reason of json dumping is we have to parse this dictionary into javascript.
        context['countries_str'] = json.dumps(COUNTRIES)
        return context