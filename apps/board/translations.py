from modeltranslation.translator import register, TranslationOptions
from .models import Board, Ses, Member, Bar, Car

@register(Board)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc',)

@register(Ses)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Member)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title',)

@register(Bar)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Car)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title',)