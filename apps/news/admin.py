from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News, New

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(New)
class NewAdmin(TranslationAdmin):
    list_display = ['title', 'desc', 'button',]