from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Banner, Home, Messages, Latest, Slide, Slides

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button_name', 'buttons_name', 'buttons_desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Messages)
class MessagesAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Latest)
class LatestAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Slide)
class SlideAdmin(TranslationAdmin):
    list_display = ['name',]
    
@admin.register(Slides)
class SlidesAdmin(TranslationAdmin):
    list_display = ['name',]
    