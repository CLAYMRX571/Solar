from modeltranslation.translator import register, TranslationOptions
from .models import Eurosun, Conf, Sun

@register(Eurosun)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Conf)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button',)

@register(Sun)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)
