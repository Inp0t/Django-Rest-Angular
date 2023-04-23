from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

class Inmueble_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direction = serializers.CharField()
    country = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()
    active = serializers.BooleanField()

    def create(self,validate_data):
        return Inmueble.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.direction = validate_data.get('direction', instance.direction)
        instance.country = validate_data.get('country', instance.country)
        instance.description = validate_data.get('description', instance.description)
        instance.image = validate_data.get('image', instance.image)
        instance.active = validate_data.get('active', instance.active)
        return instance







