from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from app.course.models import Course

User = get_user_model()


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    ratings = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.course.name_of_course
