from modeltranslation.translator import register, TranslationOptions
from .models import Eurosun

@register(Eurosun)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
