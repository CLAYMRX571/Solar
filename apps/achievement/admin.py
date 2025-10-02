from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Achievement, Recept, Past

@admin.register(Achievement)
class AchievementAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Recept)
class ReceptAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Past)
class PastAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]