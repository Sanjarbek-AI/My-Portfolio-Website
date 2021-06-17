from modeltranslation.translator import register, TranslationOptions

from blog.models import BlogModel, AuthorModel, BlogTagModel, CategoryModel


@register(AuthorModel)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(BlogTagModel)
class BlogTagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(BlogModel)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)
