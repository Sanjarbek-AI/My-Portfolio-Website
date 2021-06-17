from django.urls import path

from services.views import ServiceTemplateView

app_name = 'service'

urlpatterns = [
    path('', ServiceTemplateView.as_view(), name='service'),
]
