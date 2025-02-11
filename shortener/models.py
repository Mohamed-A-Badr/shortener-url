import random
import string
import time

from django.db import models
from django.utils.translation import gettext_lazy as _


def generate_short_code():
    random.seed(time.time())
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


class OriginalURL(models.Model):
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Original URL")
        verbose_name_plural = _("Original URLs")
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["url"])]

    def __str__(self):
        return self.url


class ShortenedURL(models.Model):
    original_url = models.ForeignKey(
        OriginalURL, related_name="shortened_url", on_delete=models.CASCADE
    )
    short_code = models.CharField(
        max_length=10, unique=True, default=generate_short_code
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Short URL")
        verbose_name_plural = _("Short URLs")
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["short_code"])]

    def get_shortened_url(self):
        return f"http://localhost:8000/api/v1/{self.short_code}"

    def __str__(self):
        return self.short_code
