from rest_framework import serializers

from .models import ShortenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    new_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.URLField(source="original_url", write_only=True)

    class Meta:
        model = ShortenedURL
        fields = ("url", "new_url")

    def get_new_url(self, obj):
        return obj.get_shortened_url()
