from django.db import models
from uuid import uuid4
from phonenumber_field.modelfields import PhoneNumberField
from backend.settings import TWILIO_ID, TWILIO_TOKEN
from twilio.rest import Client as TwilioClient

class Client(models.Model):
    name = models.CharField(
        max_length=150,
        help_text="Please enter your name",
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "clients"
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Message(models.Model):
    # message = models.TextField()
    contact_phone = PhoneNumberField(region="KZ")
    reason = models.TextField()

    def save(self, *args, **kwargs):
        print(TWILIO_ID)
        print(TWILIO_TOKEN)
        client = TwilioClient(TWILIO_ID, TWILIO_TOKEN)

        message = client.messages.create(
            body=f'Seems like I am in danger. I hear {self.reason} noise',
            from_="whatsapp:+14155238886",
            to=f'whatsapp:{self.contact_phone}' 
        )

        print(message.sid)
        return super().save(*args, **kwargs)