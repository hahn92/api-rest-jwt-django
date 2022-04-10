from rest_framework import serializers

# Custom User
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', "is_active")
