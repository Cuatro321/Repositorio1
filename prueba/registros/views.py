from django.shortcuts import render, redirect
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

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

def eliminarComentarioContacto(request,id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto,id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",{'comentarios':comentarios})
    return render(request,confirmacion,{'object':comentario})


def consultarComentarioIndividual(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    return render(request, "registros/formEditarComentario.html", {'comentario': comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('Comentarios')
    else:
        form = ComentarioContactoForm(instance=comentario)
    return render(request, "registros/formEditarComentario.html", {'comentario': comentario})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})
def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.only("matricula","nombre","carrera","turno","imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio= datetime.date(2025,7,1)
    fechaFin= datetime.date(2025,7,13)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    #Consultando entre modelos
    alumnos=Alumnos.objects.filter(comentario__coment__contains="No Inscrito")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consulta1(request):
    fechaInicio = datetime.date(2025, 7, 8)
    fechaFin = datetime.date(2025, 7, 9)
    
    comentarios = ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin))
    
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})  
def consulta2(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains="comentario")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def consulta3(request):
    comentarios = ComentarioContacto.objects.filter(usuario__icontains="Juan Perez")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def consulta4(request):
    comentarios = ComentarioContacto.objects.only("mensaje")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def consulta5(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__endswith="gracias")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})


def  archivos (request):
    if request.method == 'POST':
        form = FormArchivos(request.POST,request.FILES)
        if form.is_invalid():
            titulo= request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,archivo=archivo)
            insert.save()
            return render(request="registros/archivos.html")
        else: 
            messages.error(request,"Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})