from modeltranslation.translator import register, TranslationOptions

from about.models import FactsModel, TeamModel


@register(FactsModel)
class FactsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TeamModel)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'job',)