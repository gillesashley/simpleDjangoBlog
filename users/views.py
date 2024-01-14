from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class UserViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
