from django.urls import path

from home.views import HomeTemplateView

app_name = 'home'
urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home')
]
