from django.shortcuts import render
from Articulos.models import Entrada,Comentario
from Articulos.forms import ComentarioForm
# Create your views here.

def home(request):
    articulos = Entrada.objects.all()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():         
            nombre = form.cleaned_data['nombre']
            comentario = form.cleaned_data['comentario']
            obj = Comentario(nombre = nombre, mensaje = comentario)#carga el obj con los datos ingresados
            obj.save()#guarda el obj en la base de datos
            form = ComentarioForm()#limpia el formulario despues del ingreso
            mensaje = "Gracias por tu mensaje"
            return render(request,"bienvenida.html", {"articulo":articulos, "mensaje": mensaje, "form": form})#si entra al if return esto la html
    form = ComentarioForm()
    return render(request, "bienvenida.html", {"articulos":articulos, "form":form})#todos los articulos mandalos al template

