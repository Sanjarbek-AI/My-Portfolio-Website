from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CourseModel(models.Model):
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

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class CourseVideoModel(models.Model):
    course = models.ForeignKey(
        CourseModel,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name=_('course')
    )

    video = models.FileField(
        upload_to='course video',
        null=True, blank=True,
        verbose_name=_('video')
    )

    def __str__(self):
        return self.course.name

    class Meta:
        verbose_name = _('course video')
        verbose_name_plural = _('course videos')
