from rest_framework import viewsets, permissions, mixins, response
from .serializers import UserSerializer, PostSerializer
from .models import CustomUser, Post


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return CustomUser.objects.all().select_related('profile')


class PostViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return response.Response('Operation NOT Allowed')
