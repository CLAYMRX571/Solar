from modeltranslation.translator import register, TranslationOptions
from .models import Advance

@register(Advance)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'topic', 'performance',)
