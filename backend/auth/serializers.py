from client.models import Client
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.serializerfields import PhoneNumberField

class RegisterSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(write_only=True)
    trusted_contact_phone = PhoneNumberField(write_only=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Client
        fields = ('username', 'password', 'password2', 'phone', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        if attrs['phone'] == attrs['trusted_contact_phone']:
            raise serializers.ValidationError({"phone number": "Clients phone and trusted contacts phone cannot be the same."})
        return attrs

    def create(self, validated_data):
        client = Client.objects.create(
            username=validated_data['username'],
            phone=validated_date['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        client.set_password(validated_data['password'])
        client.save()

        return client
