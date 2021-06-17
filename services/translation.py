from modeltranslation.translator import register, TranslationOptions

from services.models import ServiceModel


@register(ServiceModel)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('best_for', 'benefits', 'position')
