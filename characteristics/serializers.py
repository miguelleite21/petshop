from rest_framework import serializers, status
from uuid import uuid4
from characteristics.models import Characteristics


class CharacteristicsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        characteristic, create = Characteristics.objects.get_or_create(**validated_data)
        if not create:
            raise ValueError(
                {"message":"characteristic already exists"},status.HTTP_409_CONFLICT
            )

        return characteristic