from modeltranslation.translator import register, TranslationOptions
from .models import About, Key

@register(About)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Key)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'title', 'ches',)