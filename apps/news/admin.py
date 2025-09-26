from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['category_name', 'all_name', 'title', 'desc',]