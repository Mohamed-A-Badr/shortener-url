from rest_framework import serializers

from .models import ShortenedURL, OriginalURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    url = serializers.URLField(write_only=True)
    new_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ShortenedURL
        fields = (
            "url",
            "new_url",
        )

    def create(self, validated_data):
        original_url, created = OriginalURL.objects.get_or_create(
            url=validated_data["url"]
        )

        shortened_url = ShortenedURL.objects.create(original_url=original_url)

        return shortened_url

    def get_new_url(self, obj):
        return obj.get_shortened_url()
