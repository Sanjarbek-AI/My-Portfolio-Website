from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from blog.models import AuthorModel, BlogTagModel, CategoryModel, BlogImageModel, BlogModel, CommentModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(AuthorModel)
class AuthorModelAdmin(MyTranslationAdmin):
    search_fields = ['name']
    list_display = ['name', 'created_at']
    list_filter = ['created_at']


@admin.register(BlogTagModel)
class BlogTagModelAdmin(MyTranslationAdmin):
    search_fields = ['name']
    list_display = ['name', 'created_at']
    list_filter = ['created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    search_fields = ['name']
    list_display = ['name', 'created_at']
    list_filter = ['created_at']


class BlogImagesStackedInline(admin.StackedInline):
    model = BlogImageModel


@admin.register(BlogModel)
class BlogModelAdmin(MyTranslationAdmin):
    search_fields = ['title', 'short_description']
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    inlines = [BlogImagesStackedInline]
    autocomplete_fields = ['tags', 'categories']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'comment']
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
