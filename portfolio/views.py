from django.views.generic import TemplateView, ListView, DetailView

from portfolio.models import PortfolioModel


class PortfolioListView(ListView):
    template_name = 'portfolio-grid.html'

    def get_queryset(self):
        return PortfolioModel.objects.order_by('-pk')


class PortfolioDetailView(DetailView):
    template_name = 'portfolio-details.html'
    model = PortfolioModel

