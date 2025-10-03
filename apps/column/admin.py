from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Column, Data, Mons

@admin.register(Column)
class ColumnAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Data)
class DataAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Mons)
class MonsAdmin(TranslationAdmin):
    list_display = ['name',]