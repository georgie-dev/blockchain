from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .models import User, CryptoData
from .serializers import DataSerializer


@api_view(['POST', 'PATCH'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        user_id = request.data.get('id')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        user = None
        if '0x' in email:
            try:
                user = User.objects.get(wallet=email)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(email=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'token': token.key,
                    'email': user.email,
                    'wallet': user.wallet,
                    'nationality': user.nationality
                }
                , status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class cryptoDataSet(viewsets.ModelViewSet):
    queryset = CryptoData.objects.all()
    serializer_class = DataSerializer
