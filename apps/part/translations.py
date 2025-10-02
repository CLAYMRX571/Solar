from modeltranslation.translator import register, TranslationOptions
from .models import Part, Cards, Pord

@register(Part)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc',)

@register(Cards)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Pord)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'desc',)