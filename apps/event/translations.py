from modeltranslation.translator import register, TranslationOptions
from .models import Event

@register(Event)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'location', 'title',)