from rest_framework import viewsets, permissions, mixins, response
from .serializers import UserSerializer
from .models import CustomUser


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return CustomUser.objects.all().select_related('profile')

    # def destroy(self, request, *args, **kwargs):
    #     return response.Response('Delete is Not Allowed')

        