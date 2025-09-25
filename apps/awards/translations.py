from modeltranslation.translator import register, TranslationOptions
from .models import Award

@register(Award)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)