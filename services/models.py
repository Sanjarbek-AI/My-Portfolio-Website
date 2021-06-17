from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ServiceModel(models.Model):
    time = models.CharField(max_length=20, verbose_name=_('time'))
    price = models.IntegerField(verbose_name=_('price'))
    position = models.CharField(max_length=20, verbose_name=_('position'))
    best_for = models.CharField(max_length=30, verbose_name=_('best_for'))
    benefits = RichTextUploadingField(verbose_name=_('benefits'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.best_for

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')
