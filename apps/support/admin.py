from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Support, Miss, Invol

@admin.register(Support)
class SupportAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title',]

@admin.register(Miss)
class MissAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Invol)
class InvolAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'link',]