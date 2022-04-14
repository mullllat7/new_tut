from django.shortcuts import render
from rest_framework import generics

from app.category.models import Category
from app.category.permissions import IsActivePermission
from app.category.serializers import CategorySerializers, CategoryDetailSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsActivePermission]


class CategoryDetailView(generics.RetrieveAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsActivePermission]
