from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.course.views import CourseDetailView, CourseLikeViewSet, SavedView, CourseViewSet
#
router = DefaultRouter()
router.register('like', CourseLikeViewSet)
router.register('', CourseViewSet)
# router.register('saved-list', SavedView)


urlpatterns = [
    path('savedlist/', SavedView.as_view()),
    path('<int:pk>/', CourseDetailView.as_view()),
    path('', include(router.urls)),
]
urlpatterns.extend(router.urls)
