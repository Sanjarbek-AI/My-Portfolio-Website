from django.urls import path

from portfolio.views import PortfolioListView, PortfolioDetailView

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioListView.as_view(), name='list'),
    path('detail/<int:pk>', PortfolioDetailView.as_view(), name='detail'),
]
