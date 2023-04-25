
from django.urls  import path
#from inmuebleslist_app.api.views import inmueble_list
#from inmuebleslist_app.api.views import inmueble_detail
from inmuebleslist_app.api.views import InmuebleDetalleAV, InmuebleListAV

urlpatterns = [
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'),
    path('<int:pk>', InmuebleDetalleAV.as_view(), name='inmueble-detail'),

]
