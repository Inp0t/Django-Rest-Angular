
from django.urls  import path
from inmuebleslist_app.api.views import inmueble_list
from inmuebleslist_app.api.views import inmueble_detail

urlpatterns = [
    path('list/', inmueble_list, name='inmueble-list'),
    path('<int:pk>', inmueble_detail, name='inmueble-detail'),

]
