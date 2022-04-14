from rest_framework.routers import DefaultRouter

from .views import BookViewSet, AuthorViewSet


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='user')
router.register(r'author', AuthorViewSet, basename='author')

urlpatterns = router.urls