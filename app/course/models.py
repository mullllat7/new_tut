from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from app.category.models import Category

User = get_user_model()


class Course(models.Model):

    name_of_course = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='course')
    # rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return self.name_of_course


class CourseImage(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_image')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.course.name_of_course


class Like(models.Model):
    user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='like', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.like


class Saved(models.Model):
    user = models.ForeignKey(User, related_name='saved_p', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='saved', on_delete=models.CASCADE)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.saved}'
