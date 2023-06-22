from django.urls import path, include
from . import views
from .views import RegistroUsuario


urlpatterns = [
    # localhost:8000/registrar
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
]