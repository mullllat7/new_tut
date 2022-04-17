from rest_framework.routers import DefaultRouter

from .views import RatingViewSet

router = DefaultRouter()
router.register('', RatingViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)
