from uuid import uuid4
from rest_framework import serializers,status
from animals.models import Animals
from groups.models import Groups

class GroupsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        animals = validated_data.pop("animals")
        group = Groups.objects.create(**validated_data)
        for animal in animals:
            animal= Animals.objects.get(**animal)
            group.animals.add(animal)
        return group


    def update(self, instance, validated_data):

        for key,value in validated_data.items():
            setattr(instance,key,value)
            instance.save()

        return instance