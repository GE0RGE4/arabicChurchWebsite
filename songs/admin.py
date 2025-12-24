from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'lyrics')

    class Media:
        css = {
            'all': ('songs/css/rtl.css',)  # note: path is relative to static/
        }

# Unregister first if already registered
try:
    admin.site.unregister(Song)
except admin.sites.NotRegistered:
    pass

# Register properly
admin.site.register(Song, SongAdmin)
