from modeltranslation.translator import register, TranslationOptions
from .models import Public, Pub

@register(Public)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'topic', 'link',)

@register(Pub)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button',)
