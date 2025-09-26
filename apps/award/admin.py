from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Award

@admin.register(Award)
class AwardAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]
