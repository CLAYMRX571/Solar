from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Part, Cards, Pord

@admin.register(Part)
class PartAdmin(TranslationAdmin):
    list_display = ['desc',]

@admin.register(Cards)
class CardsAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Pord)
class PordAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'desc',]
