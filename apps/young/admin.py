from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Young, Fol, Met, Pic

@admin.register(Young)
class YoungAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Fol)
class FolAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'link',]

@admin.register(Met)
class MetAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

@admin.register(Pic)
class PicAdmin(TranslationAdmin):
    list_display = ['name',]