from modeltranslation.translator import register, TranslationOptions
from .models import Support, Miss, Invol

@register(Support)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'title',)

@register(Miss)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Invol)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'link',)