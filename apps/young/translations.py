from modeltranslation.translator import register, TranslationOptions
from .models import Young, Fol, Met, Pic
    
@register(Young)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Fol)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'link',)

@register(Met)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button',)

@register(Pic)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)