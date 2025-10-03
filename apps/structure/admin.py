from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Structure, Column, Card

@admin.register(Structure)
class StructureAdmin(TranslationAdmin):
    list_display = ['desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Column)
class ColumnAdmin(TranslationAdmin):
    list_display = ['desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Card)
class CardAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }
