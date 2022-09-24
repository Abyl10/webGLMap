from client.models import Client
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Client
        fields = ('name', 'password', 'password2', 'email')
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        client = Client.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
        )

        client.set_password(validated_data['password'])
        client.save()

        return client
