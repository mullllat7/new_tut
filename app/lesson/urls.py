from django.urls import path

from app.lesson.views import LessonListView, LessonDetailView

urlpatterns = [
    path('lesson-list/', LessonListView.as_view()),
    path('lesson-list/<int:pk>/', LessonDetailView.as_view()),
]
