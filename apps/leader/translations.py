from modeltranslation.translator import register, TranslationOptions
from .models import Leader, Cont, Win

@register(Leader)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Cont)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Win)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)