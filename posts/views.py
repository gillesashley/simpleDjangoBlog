from rest_framework.viewsets import ModelViewSet

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer
