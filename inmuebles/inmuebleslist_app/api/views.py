from rest_framework.response import Response
from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import Inmueble
# from rest_framework.decorators import api_view
from rest_framework import status
from inmuebleslist_app.api.serializers import Inmueble_serializer
from rest_framework.views import APIView


class InmuebleListAV(APIView):
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        serializer = Inmueble_serializer(inmuebles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Inmueble_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class InmuebleDetalleAV(APIView):
    def get(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = Inmueble_serializer(inmueble)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = Inmueble_serializer(inmueble, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
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
        try:
            inmueble = Inmueble.objects.get(pk=pk)
            serializer = Inmueble_serializer(inmueble)
            return Response(serializer.data)
        except Inmueble.DoesNotExist:
            return Response({'Error': 'El Inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        inmueble = Inmueble.objects.get(pk=pk)
        de_serializer = Inmueble_serializer(inmueble, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:

            inmueble = Inmueble.objects.get(pk=pk)
            inmueble.delete()
        except Inmueble.DoesNotExist:
            return Response({'Error': 'El Inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)
"""
