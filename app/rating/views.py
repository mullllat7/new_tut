from django.shortcuts import render
from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from app.account.permissions import IsActivePermission
from app.rating.models import Rating
from app.rating.serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsActivePermission]

    def get_serializer_context(self):
        return {'request': self.request}
