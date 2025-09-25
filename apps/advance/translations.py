from modeltranslation.translator import register, TranslationOptions
from .models import Advance

@register(Advance)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'see_more', 'category_name', 'desc', 'edu_name', 'edu_desc',)
