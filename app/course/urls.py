from django.urls import path
from rest_framework.routers import DefaultRouter

from app.course.views import CourseListView, CourseDetailView, CourseLikeViewSet
#
router = DefaultRouter()
router.register('course-list', CourseLikeViewSet)

urlpatterns = [
    path('course-list/', CourseListView.as_view()),
    path('course-list/<int:pk>/', CourseDetailView.as_view()),
    # path('course-list/<int:pk>/like/', CourseLikeViewSet.as_view),

]
urlpatterns.extend(router.urls)
