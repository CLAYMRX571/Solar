from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Daniel, Recep

@admin.register(Daniel)
class DanielAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Recep)
class RecepAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }