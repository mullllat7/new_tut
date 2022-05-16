# from time import timezone
# from datetime import timezone
# from time import timezone

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from app.course.models import Course


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='lesson')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Video(models.Model):

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_video')
    video = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.lesson.name

