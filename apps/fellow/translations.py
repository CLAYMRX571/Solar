from modeltranslation.translator import register, TranslationOptions
from .models import Fellow, Well, Lars, Gallery, Cent, Run

@register(Fellow)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'title',)

@register(Well)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Lars)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Gallery)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Cent)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'title', 'bio',)

@register(Run)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)