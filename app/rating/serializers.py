from rest_framework.serializers import ModelSerializer

from app.rating.models import Rating


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        ratings = Rating.objects.create(**validated_data)
        return ratings

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = f'{instance.author}'

        return representation

