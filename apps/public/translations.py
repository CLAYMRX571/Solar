from modeltranslation.translator import register, TranslationOptions
from .models import Public

@register(Public)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
