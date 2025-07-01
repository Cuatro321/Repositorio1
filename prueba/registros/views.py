from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
#Accedemos al modelo Alumnos que contine la estructura de la tabla

# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
      #all recupera todos los objetos del modelo (registros de la tabla alumnos)  
    return render(request,"registros/principal.html",{'alumnos':alumnos})
    #Indicamos el lugar donde se renderizará el resultado de esta bista 
    #y enviamos la lista de alumnos recuperados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save()
            return render(request,'registros/contacto.html')
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form':form})

def contacto(request):
    return render(request,"registros/contacto.html")
    #Indicamos el lugar donde se renderizara el resultado de esta vista