from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Event, Text, Greeb

@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'area', 'part', 'contact',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Text)
class TextAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Greeb)
class GreebAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }