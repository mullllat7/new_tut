from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from app.course.models import Course, CourseImage, Like, Saved
from app.rating.serializers import RatingSerializer


class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation


class CourseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = CourseImageSerializer(CourseImage.objects.filter(course=instance.id, ), many=True,
                                                 context=self.context).data
        representation['like'] = instance.like.filter(like=True).count()
        total_rating = [i.ratings for i in instance.ratings.all()]

        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        # representation['total_rating'] = RatingSerializer(instance.rating.filter(course=instance.id), many=True).data
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


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['like'] = instance.like.filter(like=True).count()
        return representation


class SavedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Saved
        fields = '__all__'
