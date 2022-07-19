from email.headerregistry import Group
from uuid import uuid4
from rest_framework import serializers,status
from animals.models import Animals
from characteristics.models import Characteristics
from characteristics.serializers import CharacteristicsSerializer
from groups.models import Groups
from groups.serializers import GroupsSerializer


class AnimalsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    birth_date = serializers.DateField(required=False)
    weight = serializers.FloatField()
    characteristics = CharacteristicsSerializer(many=True)
    group = GroupsSerializer()

    def create(self, validated_data):
        characteristics = validated_data.pop("characteristics")
        groups = validated_data.pop("group")
        group, _ = Groups.objects.get_or_create(**groups)
        animal = Animals.objects.create(**validated_data,group = group)
       
        for characteristic in characteristics:
            characteristic, _ = Characteristics.objects.get_or_create(**characteristic)
            animal.characteristics.add(characteristic)
        return animal



    def update(self, instance, validated_data):
        non_updatable = {"group", "characteristics"}
        
        for key, value in validated_data.items():
            if key in non_updatable:
                raise KeyError(
                    {"details": f"You con 't update the `{key}` key."},
                    status.HTTP_400_BAD_REQUEST,
                )

            setattr(instance, key, value)
            instance.save()

        return instance