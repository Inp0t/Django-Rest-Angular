# from django.shortcuts import render
# from inmuebleslist_app.models import Inmueble
# from django.http import  JsonResponse
# def inmueble_list(request):
#     inmuebles = Inmueble.objects.all()
#     data = {
#         'inmuebles': list(inmuebles.values())
#     }
#
#     return JsonResponse(data)
#
# def inmueble_detail(request,pk):
#     inmueble = Inmueble.objects.get(pk=pk)
#     data = {
#         'direction': inmueble.direction,
#         'country': inmueble.country,
#         'image': inmueble.image,
#         'active': inmueble.active,
#     }
#     return JsonResponse(data)



