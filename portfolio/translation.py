from modeltranslation.translator import register, TranslationOptions

from portfolio.models import PortfolioModel


@register(PortfolioModel)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title', 'name', 'full_title', 'description')
