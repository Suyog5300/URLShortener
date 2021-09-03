from rest_framework import serializers
from URLShortenApp.models import URLShortenModel

class URLShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLShortenModel
        fields = ['id', 'original_url', 'short_code', 'updated_at', 'created_at']
        read_only_fields = ['short_code']

    def validate_original_url(self,value):
        qs = URLShortenModel.objects.filter(original_url = value)
        if qs.exists():
            raise serializers.ValidationError("Cannot Shorten URL. Shortened URL Already Exists.")
        return value
