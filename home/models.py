from django.db import models
from django.utils.translation import ugettext_lazy as _


class TestimonialModel(models.Model):
    image = models.ImageField(upload_to='testimonial', null=True, blank=True, verbose_name=_('image'))
    feedback = models.CharField(max_length=200, verbose_name=_('feedback'))
    name = models.CharField(max_length=20, verbose_name=_('name'))
    job = models.CharField(max_length=20, verbose_name=_('job'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimonials'


class ClientModel(models.Model):
    image = models.ImageField(upload_to='clients', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')
