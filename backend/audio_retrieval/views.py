from audio_retrieval.models import Audio
from audio_retrieval.serializers import AudioSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

class AudioView(APIView): # get the songs
    def get(self, request, format=None):
        serializer = AudioSerializer(Audio.objects.all(), many=True)
        return Response(serializer.data) 