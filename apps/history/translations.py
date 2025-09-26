from modeltranslation.translator import register, TranslationOptions
from .models import History

@register(History)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'policy_desc',)