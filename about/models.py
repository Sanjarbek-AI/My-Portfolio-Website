from django.db import models
from django.utils.translation import ugettext_lazy as _


class FactsModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    number = models.IntegerField(verbose_name=_('number'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('fact')
        verbose_name_plural = _('facts')


class TeamModel(models.Model):
    image = models.ImageField(upload_to='team', verbose_name=_('image'))
    name = models.CharField(max_length=30, verbose_name=_('name'))
    job = models.CharField(max_length=30, verbose_name=_('job'))
    instagram = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('instagram'))
    facebook = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('facebook'))
    twitter = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('twitter'))
    linked = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('linked'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')
