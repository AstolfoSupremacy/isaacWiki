from django.urls import path, include
from . import views
from .views import RegistroUsuario

urlpatterns = [
    path('', views.home, name= "home"),
    path('bosses', views.bosses, name="bosses"), 
    path('items', views.items, name="items"), 
    path('personajes', views.personajes, name="personajes"), 
    path('servicio_web', views.servicio_web, name="servicio_web"), 
    path('formulario', views.formulario, name="index2"), 
    path('listar_trinket', views.listar_trinket, name="listar_trinket"), 
    path('agregar_trinket', views.agregar_trinket, name="agregar_trinket"),
    path('editar_trinket/<int:carrera_id>', views.editar_trinket ,name="editar_trinket"),
    path('borrar_trinket/<int:carrera_id>', views.borrar_trinket, name="borrar_trinket"),
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
]


