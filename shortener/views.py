from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.response import Response

from .models import ShortenedURL
from .serializers import ShortenedURLSerializer


class ShortURLView(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class RedirectToWebsiteView(generics.GenericAPIView):
    def get(self, request, short_code):
        cached_url = cache.get(f"short_url:{short_code}")
        if cached_url:
            return redirect(cached_url)

        instance = get_object_or_404(ShortenedURL, short_code=short_code)
        cache.set(
            f"short_url:{short_code}",
            instance.original_url,
            timeout=3600,
        )
        return redirect(instance.original_url)


short_url = ShortURLView.as_view()
redirect_to_website = RedirectToWebsiteView.as_view()
