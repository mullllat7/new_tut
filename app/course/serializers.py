from rest_framework import serializers

from app.course.models import Course, CourseImage, Like


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