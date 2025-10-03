from modeltranslation.translator import register, TranslationOptions
from .models import Challenge, Anno, Wins

@register(Challenge)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',) 

@register(Anno)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc',) 

@register(Wins)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'title',) 