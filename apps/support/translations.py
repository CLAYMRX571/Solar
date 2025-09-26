from modeltranslation.translator import register, TranslationOptions
from .models import Support

@register(Support)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)