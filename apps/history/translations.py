from modeltranslation.translator import register, TranslationOptions
from .models import History, Coll, Greed

@register(History)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc',)

@register(Coll)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc',)

@register(Greed)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)