from modeltranslation.translator import register, TranslationOptions

from home.models import TestimonialModel


@register(TestimonialModel)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('name', 'job', 'feedback',)
