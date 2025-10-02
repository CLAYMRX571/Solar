from modeltranslation.translator import register, TranslationOptions
from .models import Award, Link

@register(Award)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc',)

@register(Link)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'awards', 'achieve', 'lead', 'fell', 'chall', 'jour',)