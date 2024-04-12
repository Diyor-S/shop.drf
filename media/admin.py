from django.contrib import admin
from media.models import *


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'file_type']
    list_filter = ['file_type']
    search_fields = ['file_type']

@admin.register(CommonSettings)
class CommonSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_phone_number']
