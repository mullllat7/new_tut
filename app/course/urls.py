from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.course.views import CourseListView, CourseDetailView, CourseLikeViewSet, SavedView, CourseViewSet
#
router = DefaultRouter()
router.register('', CourseLikeViewSet)
router.register('', CourseViewSet)

urlpatterns = [
    path('course-list/', CourseListView.as_view()),
    path('course-list/<int:pk>/', CourseDetailView.as_view()),
    path('saved-list/', SavedView.as_view()),
    path('', include(router.urls)),
    # path('course-list/<int:pk>/like/', CourseLikeViewSet.as_view),

]
urlpatterns.extend(router.urls)
