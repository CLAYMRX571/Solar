from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Fellow

@admin.register(Fellow)
class FellowAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'focus_name', 'focus_desc',]
