from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics

from .models import ShortenedURL
from .serializers import ShortenedURLSerializer


class ShortURLView(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer


class RedirectToWebsiteView(generics.GenericAPIView):
    def get(self, request, short_code):
        cached_url = cache.get(f"short_url:{short_code}")
        if cached_url:
            return redirect(cached_url)

        instance = get_object_or_404(ShortenedURL, short_code=short_code)
        cache.set(
            f"short_url:{short_code}",
            instance.original_url.url,
            timeout=86400,
        )
        return redirect(instance.original_url.url)


short_url = ShortURLView.as_view()
redirect_to_website = RedirectToWebsiteView.as_view()
