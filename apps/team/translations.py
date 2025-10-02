from modeltranslation.translator import register, TranslationOptions
from .models import Team, Cd

@register(Team)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button',)

@register(Cd)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title',)