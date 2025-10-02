from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import History, Coll, Greed

@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    list_display = ['desc',]

@admin.register(Coll)
class CollAdmin(TranslationAdmin):
    list_display = ['desc',]

@admin.register(Greed)
class GreedAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]
