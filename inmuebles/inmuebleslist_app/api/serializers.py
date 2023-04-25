from rest_framework import serializers
from inmuebleslist_app.models import Inmueble


def column_longitud(value):
    if len(value) < 2:
        raise serializers.ValidationError('El valor ingresado es muy corto.')


class Inmueble_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direction = serializers.CharField(validators=[column_longitud])
    country = serializers.CharField(validators=[column_longitud])
    description = serializers.CharField()
    image = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validate_data):
        return Inmueble.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.direction = validate_data.get('direction', instance.direction)
        instance.country = validate_data.get('country', instance.country)
        instance.description = validate_data.get('description', instance.description)
        instance.image = validate_data.get('image', instance.image)
        instance.active = validate_data.get('active', instance.active)
        return instance

    def validate(self, data):
        if data['direction'] == data['country']:
            raise serializers.ValidationError('La dirección y el pais deben ser diferentes')
        else:
            return data

    def validate_image(self, data):
        if len(data) < 2:
            raise serializers.ValidationError('La url de la imagen es muy corta')
        else:
            return data

