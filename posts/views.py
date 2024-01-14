from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



