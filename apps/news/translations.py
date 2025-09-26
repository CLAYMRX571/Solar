from modeltranslation.translator import register, TranslationOptions
from .models import News

@register(News)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'all_name', 'title', 'desc',)