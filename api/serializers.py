from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Account

class AccountStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username', 'telegram_id')

    def validate_telegram_id(self, telegram_id):
        if Account.objects.filter(telegram_id=telegram_id).exists():
            data = {
                'success': False,
                'message': 'Telegram ID already registered',
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)

class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'