from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer

# Custom User
from django.contrib.auth import get_user_model
User = get_user_model()


class ListUsersAPIView(APIView):
    """
    - Consulta Usuario
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        user = User.objects.get(id=self.request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)