from django.urls import path
from audio_retrieval.views import AudioView

urlpatterns = [
    path('audio/', AudioView.as_view(), name='audio')
]
