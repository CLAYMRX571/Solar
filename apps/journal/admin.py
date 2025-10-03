from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Journal, Table, Detail, Text

@admin.register(Journal)
class JournalAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Table)
class TableAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Detail)
class DetailAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Text)
class TextAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'list',]