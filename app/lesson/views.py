from rest_framework import generics, viewsets
from django.shortcuts import render

from app.account.permissions import IsActivePermission
from app.lesson.models import Lesson
from app.lesson.serializers import LessonSerializers, LessonDetailSerializer


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsActivePermission]

    def get_serializer_context(self):
        return {'request': self.request}


class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsActivePermission, ]

