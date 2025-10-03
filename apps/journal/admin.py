from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
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

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Text)
class TextAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'list',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }