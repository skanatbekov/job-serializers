from rest_framework import serializers

from .models import Position, Employee


class PositionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    position_name = serializers.CharField()
    department = serializers.CharField()

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.position_name = validated_data['position_name'],
        instance.department = validated_data['department']
        instance.save()
        return instance


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField()
    birth_date = serializers.DateField()
    position = PositionSerializer()
    wage = serializers.IntegerField()

    def create(self, validated_data):
        position = Position.objects.get(id)
        return Employee.objects.create(position=position, **validated_data)

    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname'],
        instance.birth_date = validated_data['birth_date'],
        instance.position = Position.objects.get(id),
        instance.wage = validated_data['wage']
        instance.save()
        return instance
