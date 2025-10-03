from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Fellow, Well, Lars, Gallery, Cent, Run

@admin.register(Fellow)
class FellowAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Well)
class WellAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Lars)
class LarsAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Cent)
class CentAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title', 'bio',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Run)
class RunAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }
