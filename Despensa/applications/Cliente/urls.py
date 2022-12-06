from django.contrib import admin
from django.urls import path, re_path, include
from . import views
app_name = "cliente_app"

urlpatterns = [
    path(
        'cliente/',
        views.Cliente.as_view(),
        name='Pagina cliente'
    ),
    path(
        'lista/',
        views.ClienteListView.as_view(),
        name='Lista de Clientes'
    ),

    path(
        'buscar/',
        views.BuscarClienteListView.as_view(),
        name='Buscar Clientes'
    ),

    path(
        'detalle/<pk>/',#<pk>/ se usa para decirle que registro voy a eliminar es el id del cliente
        views.ClienteDetailView.as_view(),
        name='Detalle del cliente'
    ),

    path(
        'create/',
        views.ClienteCreateView.as_view(),
        name='Alta de Clientes'
    ),

    path(
        'update/<pk>/',
        views.ClienteUpdateView.as_view(),
        name='Modificar Cliente'
    ),
]