from django.shortcuts import render
from django.views.generic import TemplateView

from about.models import TeamModel, FactsModel


class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = TeamModel.objects.all()
        context['facts'] = FactsModel.objects.all()
        return context
