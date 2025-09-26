from modeltranslation.translator import register, TranslationOptions
from .models import Museum

@register(Museum)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'members_title', 'disclaimer_name', 'disclaimer_desc',)