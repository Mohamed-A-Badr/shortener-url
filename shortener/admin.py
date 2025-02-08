from django.contrib import admin

from .models import ShortenedURL

# Register your models here.


@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "short_code", "created_at")
    list_filter = ("created_at",)
    search_fields = ("short_code", "original_url")

    def url(self, obj):
        return (
            obj.original_url[:20] + "......"
            if len(obj.original_url) > 20
            else obj.original_url
        )

    url.short_description = "URL"
