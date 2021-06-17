from modeltranslation.translator import register, TranslationOptions

from menu.models import CourseModel


@register(CourseModel)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'full_title', 'description', 'solution')