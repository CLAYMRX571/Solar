from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Award, Link

@admin.register(Award)
class AwardAdmin(TranslationAdmin):
    list_display = ['desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Link)
class LinkAdmin(TranslationAdmin):
    list_display = ['name', 'awards', 'achieve', 'lead', 'fell', 'chall', 'jour',]