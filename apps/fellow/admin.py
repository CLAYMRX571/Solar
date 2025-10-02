from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Fellow, Well, Lars, Gallery, Cent, Run

@admin.register(Fellow)
class FellowAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title',]

@admin.register(Well)
class WellAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Lars)
class LarsAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Cent)
class CentAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title', 'bio',]

@admin.register(Run)
class RunAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]
