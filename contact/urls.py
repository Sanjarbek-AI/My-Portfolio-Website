from django.urls import path

from contact.views import ContactCreateView

app_name = 'contact'

urlpatterns = [
    path('', ContactCreateView.as_view(), name='contact')
]
