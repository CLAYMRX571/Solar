from modeltranslation.translator import register, TranslationOptions
from .models import News, New

@register(News)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(New)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'button',)