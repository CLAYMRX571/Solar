from modeltranslation.translator import register, TranslationOptions
from .models import Jobs

@register(Jobs)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'long_desc',)