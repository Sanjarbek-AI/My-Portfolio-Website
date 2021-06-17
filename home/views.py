from django.views.generic import TemplateView

from about.models import FactsModel
from home.models import TestimonialModel, ClientModel
from portfolio.models import PortfolioModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['testimonials'] = TestimonialModel.objects.all()
        context['facts'] = FactsModel.objects.all()
        context['clients'] = ClientModel.objects.all()
        return context
