from django.contrib import admin

from .models import ShortenedURL, OriginalURL

# Register your models here.


@admin.register(OriginalURL)
class OriginalURLAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "truncated_url",
        "created_at",
    )
    list_filter = ("created_at",)
    search_fields = ("url",)

    def truncated_url(self, obj):
        return obj.url[:50] + "......" if len(obj.url) > 50 else obj.url

    truncated_url.short_description = "URL"


@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "short_code", "created_at")
    list_filter = ("created_at",)
    search_fields = ("short_code",)
    raw_id_fields = ("original_url",)

    def url(self, obj):
        return obj.original_url.id

    url.short_description = "URL"
