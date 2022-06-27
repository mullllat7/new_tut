from django.utils.timezone import now

import django_filters
from rest_framework import generics, viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app.account.permissions import IsActivePermission
from app.course.models import Course, Like, Saved, UserCourseViewed
from app.course.permissions import IsAuthor
from app.course.serializers import CourseSerializers, CourseDetailSerializer, SavedSerializer, LikeSerializer
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin

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



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticated, ]
    
    def get_object(self):
        print("---------------")
        obj = super().get_object()
        user = self.request.user
        if user.is_authenticated:
            course_view, _ = UserCourseViewed.objects.get_or_create(
                user=user,
                course=obj
            )
            course_view.timestamp = now()
            course_view.save()
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CourseDetailSerializer(instance)
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def like(self, request, pk):
        course = self.get_object()
        like_obj, _ = Like.objects.get_or_create(course=course, author=request.user)
        print(like_obj)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'liked'
        if not like_obj.like:
            status = 'unliked'
        return Response({'status': status})

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
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):

        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(user=user, saved=True)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CourseHistoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializers

    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.filter(
            viewed__user=user
        ).order_by('-viewed__timestamp')

        return queryset