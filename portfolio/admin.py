from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from portfolio.models import PortfolioModel, PortfolioImageModel


class PortfolioImageStackedInline(admin.StackedInline):
    model = PortfolioImageModel


@admin.register(PortfolioModel)
class PortfolioModelAdmin(TranslationAdmin):
    search_fields = ['title', 'name']
    list_display = ['name', 'title', 'created_at']
    list_filter = ['name', 'title']
    inlines = [PortfolioImageStackedInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
