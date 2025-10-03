from modeltranslation.translator import register, TranslationOptions
from .models import Museum, Ms, Mega, Supa

@register(Museum)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Ms)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button',)

@register(Mega)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Supa)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button',)