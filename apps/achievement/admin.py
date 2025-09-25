from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Achievement

@admin.register(Achievement)
class AchievementAdmin(TranslationAdmin):
    list_display = ['name', 'see_more', 'category_name', 'desc', 'edu_name', 'edu_desc',]