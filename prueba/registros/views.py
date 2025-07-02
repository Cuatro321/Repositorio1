from django.shortcuts import render, redirect
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm

# Vista para mostrar todos los alumnos
def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

# Vista para mostrar formulario de contacto y guardar comentarios
def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Comentarios') 
    else:
        form = ComentarioContactoForm()
    
    return render(request, 'registros/contacto.html', {'form': form})

# Vista para mostrar los comentarios guardados
def comentarios(request):
    lista = ComentarioContacto.objects.all()
    return render(request, 'registros/comentarios.html', {
        'comentarios': lista
    })
