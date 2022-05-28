import django_filters
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from app.account.permissions import IsActivePermission
from app.course.models import Course, Like, Saved
from app.course.permissions import IsAuthorPermission
from django_filters.rest_framework import DjangoFilterBackend
from app.course.serializers import CourseSerializers, CourseDetailSerializer, SavedSerializer
from rest_framework.views import APIView

class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, ]
        else:
            permissions = []
        return [permission() for permission in permissions]


class CourseFilter(django_filters.FilterSet):
    course = django_filters.CharFilter(field_name='name_of_course')

    class Meta:
        model = Course
        fields = ['name_of_course']


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
            permissions = [IsAuthorPermission, ]
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


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'saved':
            permissions = [IsAuthenticated, ]
        else:
            permissions = [IsAuthenticated]
        return [permissions() for permissions in permissions]

    @action(detail=True, methods=['POST'])
    def saved(self, requests, *args, **kwargs):
        course = self.get_object()
        saved_obj, _ = Saved.objects.get_or_create(course=course, user=requests.user)
        saved_obj.saved = not saved_obj.saved
        saved_obj.save()
        status = 'Сохранено в избранные'
        if not saved_obj.saved:
            status = 'Удалено из избранных'
        return Response({'status': status})

    def get_serializer_context(self):
        return {'request': self.request}


class SavedView(generics.ListAPIView):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer

