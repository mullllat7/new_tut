from rest_framework import serializers

from app.category.models import Category


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['id'] = CategorySerializers(Category.objects.filter(category=instance.id, ),
        #                                            context=self.context).data
        return representation


class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['id'] = CategorySerializers(Category.objects.filter(category=instance.id,), context = self.context).data
        return representation