from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Incore, Core, Tess

@admin.register(Incore)
class IncoreAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Core)
class CoreAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'core_name', 'core_desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Tess)
class TessAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }
