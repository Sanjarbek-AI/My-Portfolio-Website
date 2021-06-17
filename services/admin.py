from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from services.models import ServiceModel


@admin.register(ServiceModel)
class ServiceModelAdmin(TranslationAdmin):
    search_fields = ['best_for']
    list_display = ['price', 'position', 'created_at']
    list_filter = ['created_at']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
