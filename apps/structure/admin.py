from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Structure, Column, Card

@admin.register(Structure)
class StructureAdmin(TranslationAdmin):
    list_display = ['desc',]

@admin.register(Column)
class ColumnAdmin(TranslationAdmin):
    list_display = ['desc', 'button',]

@admin.register(Card)
class CardAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]
