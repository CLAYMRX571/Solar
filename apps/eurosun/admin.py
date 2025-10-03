from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Eurosun, Conf, Sun

@admin.register(Eurosun)
class EurosunAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Conf)
class ConfAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Sun)
class SunAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }