from rest_framework.routers import DefaultRouter
from .api_view import UserViewSet, PostViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('posts', PostViewSet, basename='post')

urlpatterns = router.urls
