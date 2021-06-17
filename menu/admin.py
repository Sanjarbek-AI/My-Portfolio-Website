from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from menu.models import CourseModel, CourseVideoModel


class CourseVideoStackedInline(admin.StackedInline):
    model = CourseVideoModel


@admin.register(CourseModel)
class CourseModelAdmin(TranslationAdmin):
    search_fields = ['name', 'full_title', 'title']
    list_display = ['name', 'title', 'created_at']
    list_filter = ['created_at', 'title']
    inlines = [CourseVideoStackedInline]

    class Meta:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
