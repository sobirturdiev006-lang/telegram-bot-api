from rest_framework import serializers

from .models import Account


class AccountStartSerializer(serializers.ModelSerializer):
    """Serializer for creating new user accounts from Telegram."""

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username', 'telegram_id')

    def validate_telegram_id(self, telegram_id):
        """Ensure telegram_id is unique before account creation."""
        if Account.objects.filter(telegram_id=telegram_id).exists():
            raise serializers.ValidationError(
                'Telegram ID already registered'
            )
        return telegram_id

class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'