from django.db import models
from datetime import datetime

class Audio(models.Model):
    title = models.CharField(max_length=64)
    audio_file = models.FileField()
    created_at = models.DateTimeField(default=datetime.utcnow)