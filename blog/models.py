from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AuthorModel(models.Model):
    image = models.ImageField(upload_to='author images')
    name = models.CharField(max_length=30, verbose_name=_('name'))
    description = models.TextField(null=True, blank=True, verbose_name=_('description'))
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
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class BlogTagModel(models.Model):
    name = models.CharField(max_length=15, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class CategoryModel(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class BlogModel(models.Model):
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.PROTECT,
        related_name='blogs',
        verbose_name=_('author')
    )
    tags = models.ManyToManyField(
        BlogTagModel,
        related_name='blogs',
        verbose_name=_('tags')
    )
    categories = models.ManyToManyField(
        CategoryModel,
        related_name='blogs',
        verbose_name=_('categories')
    )
    image = models.ImageField(upload_to='blog', null=True, blank=True, verbose_name=_('image'))
    title = models.CharField(max_length=50, verbose_name=_('title'))
    short_description = models.CharField(max_length=200, verbose_name=_('short_description'))
    long_description = RichTextUploadingField(verbose_name=_('long_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def get_comments(self):
        return self.comments.order_by('-created_at')

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class BlogImageModel(models.Model):
    blog = models.ForeignKey(
        BlogModel,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('blog')
    )

    image = models.ImageField(upload_to='blog images')

    def __str__(self):
        return self.blog.title

    class Meta:
        verbose_name = _('blog image')
        verbose_name_plural = _('blog images')


class CommentModel(models.Model):
    blog = models.ForeignKey(
        BlogModel,
        null=True,
        blank=True,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name=_('blog')
    )
    name = models.CharField(max_length=30, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    website = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('website'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
