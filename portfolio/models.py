from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PortfolioModel(models.Model):
    image = models.ImageField(upload_to='portfolio', verbose_name=_('image'))
    title = models.CharField(max_length=50, verbose_name=_('title'))
    name = models.CharField(max_length=50, verbose_name=_('name'))
    description = RichTextUploadingField(null=True, blank=True, verbose_name=_('description'))
    solution = RichTextUploadingField(null=True, blank=True, verbose_name=_('solution'))
    full_title = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name=_('full_title'))
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

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.title}  {self.name}'

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_previous_by_created_at()

    class Meta:
        verbose_name = _('portfolio')
        verbose_name_plural = _('portfolio')


class PortfolioImageModel(models.Model):
    portfolio = models.ForeignKey(
        PortfolioModel,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name=_('portfolio')
    )
    image = models.ImageField(upload_to='products', verbose_name=_('image'))

    def __str__(self):
        return self.portfolio.title

    class Meta:
        verbose_name = _('portfolio image')
        verbose_name_plural = _('portfolio images')
