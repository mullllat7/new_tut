from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from app.course.models import Course, CourseImage, Like, Saved
from app.lesson.models import Lesson
from app.lesson.serializers import LessonSerializers
from app.rating.serializers import RatingSerializer


class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = CourseImageSerializer(CourseImage.objects.filter(course=instance.id, ), many=True,
                                                         context=self.context).data
        representation['lessons'] = LessonSerializers(Lesson.objects.filter(course=instance.id, ), many=True,
                                                      context=self.context).data
        representation['likes'] = instance.likes.count()
        return representation


class CourseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = CourseImageSerializer(CourseImage.objects.filter(course=instance.id, ), many=True,
                                                 context=self.context).data
        representation['likes'] = instance.likes.count()
        total_rating = [i.ratings for i in instance.ratings.all()]
        representation['lessons'] = LessonSerializers(Lesson.objects.filter(course=instance.id, ), many=True,
                                                      context=self.context).data
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        return representation


class CourseImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


# class LikeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Like
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['like'] = instance.like(like=True).count()
#         return representation
class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        course = validated_data.get('course')

        if Like.objects.filter(author=user, course=course):
            like = Like.objects.get(author=user, course=course)
            return like

        like = Like.objects.create(author=user, **validated_data)
        return like




class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course'] = CourseSerializers(Course.objects.filter(id=instance.id, ), many=True,
                                                      context=self.context).data
        return representation
