from rest_framework import serializers

from app.lesson.models import Lesson,  Video


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['videos'] = LessonVideoSerializer(Video.objects.filter(lesson=instance.id, ), many=True,
                                                         context=self.context).data
        return representation


class LessonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['videos'] = LessonVideoSerializer(Video.objects.filter(lesson=instance.id, ), many=True,
                                                 context=self.context).data
        return representation


class LessonVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('video',)

    def _get_video_url(self, obj):
        if obj.video:
            url = obj.video.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['video'] = self._get_video_url(instance)
        return representation
