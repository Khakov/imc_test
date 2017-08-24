from rest_framework import serializers

from imc_test_rest.models import Animal, Area


class AnimalSerialize(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = 'id', 'name'


class AreaSerialize(serializers.ModelSerializer):
    animals = serializers.StringRelatedField(many=True)

    class Meta:
        model = Area
        fields = 'id', 'name', 'animals'
