from django.views.generic import ListView, TemplateView

from services.models import ServiceModel


class ServiceTemplateView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.order_by('-pk')
        return context
