from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Structure

@admin.register(Structure)
class StructureAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]
