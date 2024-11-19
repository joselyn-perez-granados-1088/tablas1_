from django.urls import path
from productos_app import views

urlpatterns = [
    path('',views.inicio_vista,name="gestionarProducto.html"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<codigo>",views.seleccionarProducto,name="seleccionarProducto"),
    path("borrarProducto/<codigo>",views.borrarProducto,name="borrarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto")
]
