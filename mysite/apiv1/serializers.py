from rest_framework import serializers, validators
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at', 'processed')
        read_only_fields = ('id', 'uploaded_at', 'processed')