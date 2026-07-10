from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account
from .serializers import AccountStartSerializer, AccountListSerializer


class AccountListView(generics.ListAPIView):
    """API endpoint for retrieving all registered user accounts."""
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer


class AccountStartView(APIView):
    """API endpoint for user registration via Telegram."""

    def post(self, request, *args, **kwargs):
        """
        Create a new user account.
        
        Expected fields in request body:
        - first_name (optional)
        - last_name (optional)
        - username (optional)
        - telegram_id (required, unique)
        """
        try:
            account_data = request.data
            serializer = AccountStartSerializer(data=account_data)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {
                        'status': 'success',
                        'message': 'Account successfully created',
                        'data': serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            # Handle validation errors and other exceptions
            return Response(
                {
                    'status': 'error',
                    'message': 'Account could not be created',
                    'errors': str(e) if hasattr(e, 'detail') else 'Invalid data provided'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
