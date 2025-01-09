from django.shortcuts import redirect, render

# Create your views here.
from .models import Campista
from .models import Reserva

#importando django.countrib para mensajes de confirmacion 
from django.contrib import messages

#-----------------------------------------------------------------Campista----------------------------------------------------------------
def inicio(request):
    return render(request,'inicio.html')

#Presentando en pantalla el formulario de nuevo Campista
def nuevoCampista(request):
    return render(request,'nuevoCampista.html')

#Presentando en pantalla el listado de Campista
def listadoCampista(request):
    campistaBdd=Campista.objects.all()
    return render(request,'listadoCampista.html',{'campista':campistaBdd})

#Capturando datos del formulario e insertando en la Bdd
def guardarCampista(request):
    nombreCampista=request.POST['txt_nombre']
    correoCampista=request.POST['txt_correo']
    telefonoCampista=request.POST['txt_telefono']
    direccionCampista=request.POST['txt_direccion']
    nuevoCampista=Campista.objects.create(nombreCampista=nombreCampista,
                                          correoCampista=correoCampista,telefonoCampista=telefonoCampista,
                                          direccionCampista=direccionCampista)
    messages.success(request,"Campista Insertado Exitosamente")
    return redirect('/listadoCampista')

#funcion para eliminar a Campista por ID
def eliminarCampista(request,idCam):
    eliminarCampista=Campista.objects.get(idCam=idCam)
    eliminarCampista.delete()
    messages.success(request,"Campista Eliminado")
    return redirect('/listadoCampista')

#funcion para mostrar el formulario de edicion
def editarCampista(request,idCam):
    editarCampista=Campista.objects.get(idCam=idCam)
    return render(request,"editarCampista.html", {'campista':editarCampista})

#funcion para combinar cambios de estudiantes en la bdd
def procesarEdicionCampista(request):
    campista=Campista.objects.get(idCam=request.POST['idCam'])
    nombreCampista=request.POST['txt_nombre']
    correoCampista=request.POST['txt_correo']
    telefonoCampista=request.POST['txt_telefono']
    direccionCampista=request.POST['txt_direccion']

    campista.nombreCampista=nombreCampista
    campista.correoCampista=correoCampista
    campista.telefonoCampista=telefonoCampista
    campista.direccionCampista=direccionCampista
    campista.save()
    messages.success(request,"Campista Editado Exitosamente")
    return redirect('/listadoCampista')

#-----------------------------------------------------------------Reserva------------------------------------------------------------------------------------

#Presentando en pantalla el formulario de nuevo Reserva
def nuevoReserva(request):
    campista=Campista.objects.all()
    # Renderizar el template con los datos
    return render(request,'nuevoReserva.html',{
        'campista':campista,})

#Presentando en pantalla el listado de Reserva
def listadoReserva(request):
    reservaBdd=Reserva.objects.all()
    return render(request,'listadoReserva.html',{'reserva':reservaBdd})

#Capturando datos del formulario e insertando en la Bdd
def guardarReserva(request):
    fechaInicio=request.POST['txt_fechaReservaI']
    fechaFinal=request.POST['txt_fechaReservaF']
    campista_id=request.POST['txt_nombre']
    tipoAlojamiento=request.POST['txt_tipo']
    numeroPersona=request.POST['txt_persona']
    estadoReserva=request.POST['txt_estado']
    observacionReserva=request.POST['txt_observaciones']
    campista=Campista.objects.get(idCam=campista_id)
    nuevoReserva=Reserva.objects.create(fechaInicio=fechaInicio,fechaFinal=fechaFinal,tipoAlojamiento=tipoAlojamiento,
                                        numeroPersona=numeroPersona,estadoReserva=estadoReserva,
                                        observacionReserva=observacionReserva,campista=campista)
    messages.success(request,"Reserva Insertado Exitosamente")
    return redirect('/listadoReserva')

#funcion para eliminar a Reserva por ID
def eliminarReserva(request,idRes):
    eliminarReserva=Reserva.objects.get(idRes=idRes)
    eliminarReserva.delete()
    messages.success(request,"Reserva Eliminado")
    return redirect('/listadoReserva')

#funcion para mostrar el formulario de edicion
def editarReserva(request,idRes):
    editarReserva=Reserva.objects.get(idRes=idRes)
    campista=Campista.objects.all()
    return render(request,"editarReserva.html", {
        'reserva':editarReserva,
        'campista':campista,
        })

#funcion para combinar cambios de Reserva en la bdd
def procesarEdicionReserva(request):
    reserva=Reserva.objects.get(idRes=request.POST['idRes'])
    fechaInicio=request.POST['txt_fechaReservaI']
    fechaFinal=request.POST['txt_fechaReservaF']
    campista_id=request.POST['txt_nombre']
    tipoAlojamiento=request.POST['txt_tipo']
    numeroPersona=request.POST['txt_persona']
    estadoReserva=request.POST['txt_estado']
    observacionReserva=request.POST['txt_observaciones']

    reserva.fechaInicio=fechaInicio
    reserva.fechaFinal=fechaFinal
    reserva.campista_id=campista_id
    reserva.tipoAlojamiento=tipoAlojamiento
    reserva.numeroPersona=numeroPersona
    reserva.estadoReserva=estadoReserva
    reserva.observacionReserva=observacionReserva
    reserva.save()
    messages.success(request,"Reserva Editado Exitosamente")
    return redirect('/listadoReserva')