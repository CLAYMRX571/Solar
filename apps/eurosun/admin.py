from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Eurosun, Conf, Sun

@admin.register(Eurosun)
class EurosunAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Conf)
class ConfAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

@admin.register(Sun)
class SunAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]