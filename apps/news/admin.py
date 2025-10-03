from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import News, New

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(New)
class NewAdmin(TranslationAdmin):
    list_display = ['title', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }