from django.urls import reverse
from django.views.generic import CreateView

from contact.forms import ContactModelForm


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('contact:contact')
