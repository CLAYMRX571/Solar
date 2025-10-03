from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Advance

@admin.register(Advance)
class AdvanceAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'topic', 'performance',]