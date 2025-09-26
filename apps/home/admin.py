from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Banner, Home, Latest

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button_name', 'buttons_name', 'buttons_desc',]
    
@admin.register(Latest)
class LatestAdmin(TranslationAdmin):
    list_display = ['category_name', 'browse_link_name', 'latest_title', 'latest_desc',]