from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Daniel, Recep

@admin.register(Daniel)
class DanielAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title',]

@admin.register(Recep)
class RecepAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]