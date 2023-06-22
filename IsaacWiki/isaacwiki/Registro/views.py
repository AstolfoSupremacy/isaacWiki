from django.shortcuts import render
from .models import Trinket
from .forms import TrinketForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm

# Create your views here.
def listar_trinket(request):
    trinkets = Trinket.objects.all()
    return render(request, "Registro/listar_trinket.html", {'trinkets': trinkets})

def agregar_trinket(request):
    if request.method == "POST":
        form = TrinketForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_trinket")
    else:
        form = TrinketForm()
        return render(request, "Registro/agregar_trinket.html", {'form': form})


def borrar_trinket(request, trinket_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Trinket.objects.get(id=trinket_id)
    instancia.delete()


    # Después redireccionamos de nuevo a la lista
    return redirect('listar_trinket')


def editar_trinket(request, trinket_id):
    # Recuperamos la instancia de la carrera
    instancia = Trinket.objects.get(id=trinket_id)


    # Creamos el formulario con los datos de la instancia
    form = TrinketForm(instance=instancia)


    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = TrinketForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()


    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_trinket.html", {'form': form})

def home(request):
    return render(request, 'Registro/home.html')

def bosses(request):
    return render(request, 'Registro/bosses.html')

def items(request):
    return render(request, 'Registro/items.html')

def personajes(request):
    return render(request, 'Registro/personajes.html')

def servicio_web(request):
    return render(request, 'Registro/servicio_web.html')

def formulario(request):
    return render(request, 'Registro/index2.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('home')