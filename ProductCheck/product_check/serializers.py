from rest_framework import serializers


class ProductDetailsSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)