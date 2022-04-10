from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
import jwt
from ManagerTasks.settings import SECRET_KEY

# Custom User
from django.contrib.auth import get_user_model
User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['code'] = user.username
        
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])
        validado = False
        payload = jwt.decode(attrs['refresh'], SECRET_KEY, algorithms=["HS256"])
        user = User.objects.filter(username=payload['code'])
        if user.count() > 0:
            validado = True
        
        data = {
            'access': str(refresh.access_token),
            'check': validado
        }

        return data


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer



