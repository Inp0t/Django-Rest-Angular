from rest_framework.response import Response
from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import Inmueble
from rest_framework.decorators import api_view

from inmuebleslist_app.api.serializers import Inmueble_serializer


@api_view(['GET', 'POST'])
def inmueble_list(request):
    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializer = Inmueble_serializer(inmuebles, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        de_serializer = Inmueble_serializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def inmueble_detail(request, pk):
    if request.method == 'GET':
        inmueble = Inmueble.objects.get(pk=pk)
        serializer = Inmueble_serializer(inmueble)
        return Response(serializer.data)

    if request.method == 'PUT':
        inmueble = Inmueble.objects.get(pk=pk)
        de_serializer = Inmueble_serializer(inmueble, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)

    if request.method == 'DELETE':
        inmueble = Inmueble.objects.get(pk=pk)
        inmueble.delete()
        data = {
            'result': True
        }
        return Response(data)
