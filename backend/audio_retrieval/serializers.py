from rest_framework import serializers
from audio_retrieval.models import Audio

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'