from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import History

@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'policy_desc',]
