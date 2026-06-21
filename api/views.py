from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account
from .serializers import AccountStartSerializer, AccountListSerializer


class AccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer


class AccountStartView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            account = request.data
            serializer = AccountStartSerializer(data=account)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = {
                    'status': 'success',
                    'message': 'Account successfully created',
                }
                return Response(message, status=status.HTTP_201_CREATED)
        except:
            data = {
                'status': 'error',
                'message': 'Account could not be created',
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

