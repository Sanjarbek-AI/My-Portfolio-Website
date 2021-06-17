from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from about.models import FactsModel, TeamModel


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


@admin.register(FactsModel)
class FactsModelAdmin(MyTranslationAdmin):
    search_fields = ['title']
    list_display = ['title', 'number']


@admin.register(TeamModel)
class TeamModelAdmin(MyTranslationAdmin):
    search_fields = ['name', 'job']
    list_display = ['name', 'job', 'created_at']
    list_filter = ['created_at']
