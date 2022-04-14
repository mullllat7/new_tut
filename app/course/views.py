from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.course.models import Course, Like
from app.course.permissions import IsActivePermission
from app.course.serializers import CourseSerializers, CourseDetailSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    pagination_class = PageNumberPagination
    permission_classes = [IsActivePermission]

    def get_serializer_context(self):
        return {'request':self.request}


class CourseDetailView(generics.RetrieveAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [IsActivePermission]


class CourseLikeViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'like':
            permissions = [IsAuthenticated, ]
        else:
            permissions = [IsAuthenticated, ]
        return [permissions() for permissions in permissions]

    @action(detail=True, methods=['POST'])
    def like(self, requests, *args, **kwargs):
        post = self.get_object()
        like_obj, _ = Like.objects.get_or_create(course=post, user=requests.user)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'Поставил лайк'
        if not like_obj.like:
            status = 'Убрал лайк'
        return Response({'status': status})

    def get_serializer_context(self):
        return {'request': self.request}

