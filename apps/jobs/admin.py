from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Jobs

@admin.register(Jobs)
class JobsAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'long_desc',]
