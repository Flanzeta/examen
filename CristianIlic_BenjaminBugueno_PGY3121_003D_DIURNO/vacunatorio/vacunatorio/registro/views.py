from django.shortcuts import render
from .models import Persona, Establecimiento
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def ingresar(request):
    return render(request, "ingresar.html")

def ingreso(request):
    nombre=request.GET["txt_nombre"]
    appaterno=request.GET["txt_appaterno"]
    apmaterno=request.GET["txt_apmaterno"]
    rut=request.GET["txt_rut"]
    edad=request.GET["txt_edad"]
    vacuna=request.GET["txt_vacuna"]
    fecha=request.GET["txt_fecha"]
    nombrevacunatorio=request.GET["nom_vac"]
    direccion=request.GET["dir_vac"]
    tipoestablecimiento=request.GET["tp_vac"]
    telefono=request.GET["tel_vac"]
    email=request.GET["mail_vac"]
    if len(nombre)>0 and len(appaterno)>0 and len(apmaterno)>0 and len(rut)>0 and len(edad)>0 and len(vacuna)>0 and len(fecha)>0 and len(nombrevacunatorio)>0 and len(direccion)>0 and len(tipoestablecimiento)>0 and len(telefono)>0 and len(email)>0:
        persona=Persona(nombre=nombre,appaterno=appaterno,apmaterno=apmaterno,rut=rut,edad=edad,nomvacuna=vacuna,fecha=fecha)
        persona.save()
        establecimiento=Establecimiento(nombreestablecimiento=nombrevacunatorio,tipoestablecimiento=tipoestablecimiento,direccion=direccion,telefono=telefono,email=email)
        establecimiento.save()
        mensaje="Persona Ingresada..."
    else:
        mensaje="Faltan Datos..."
        
    return HttpResponse(mensaje)
   
def listar(request):
    datos = Persona.objects.all()
    return render(request, "listar.html", {"personas":datos})

def listar_vacunatorio(request):
    datos = Establecimiento.objects.all()
    return render(request, "listarest.html", {"Establecimiento":datos})

def eliminar(request):
    id_recibido = request.GET["rut"]
    persona = Persona.objects.filter(rut=id_recibido)
    if persona:
            pro=Persona.objects.get(rut=id_recibido)
            pro.delete()
            mensaje = "Persona Eliminada..."
    else:
            mensaje = "el id recibido es " + id_recibido
    return HttpResponse(mensaje)

def eliminarest(request):
    id_recibido = request.GET["nombreestablecimiento"]
    Est= Establecimiento.objects.filter(nombreestablecimiento=id_recibido)
    if Est:
            pro2=Establecimiento.objects.get(nombreestablecimiento=id_recibido)
            pro2.delete()
            mensaje = "Establecimiento Eliminado..."
    else:
            mensaje = "el id recibido es " + id_recibido
    return HttpResponse(mensaje+"<br><a href='http://127.0.0.1:8000/'>Inicio</a>")


def buscar(request):
    return render(request, 'buscar.html')

def busqueda(request):
    datos = Persona.objects.all()
    query = request.GET["txt_busqueda"]
    busqueda = datos.filter(rut=query)
    if busqueda:
        persona = datos.get(rut=query)
        return render(request, "busqueda.html",  {"persona":persona} )
    else:
        return render(request, "busqueda.html",  {"persona":None} )
        return render(request, "busqueda.html" )

def busqueda_establecimiento(request):
    datos = Establecimiento.objects.all()
    query = request.GET["txt_busqueda_estab"]
    busqueda2 = datos.filter(nombreestablecimiento=query)
    if busqueda2:
        establecimiento = datos.get(nombreestablecimiento=query)
        return render(request, "busqueda_establecimiento.html",  {"establecimiento":establecimiento} )
    else:
        return render(request, "busqueda_establecimiento.html" )