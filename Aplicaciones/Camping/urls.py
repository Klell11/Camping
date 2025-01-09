from django.urls import path
from . import views

urlpatterns=[
    path('',views.inicio),
    path('listadoCampista/',views.listadoCampista),
    path('nuevoCampista/',views.nuevoCampista),
    path('guardarCampista/',views.guardarCampista),
    path('eliminarCampista/<idCam>',views.eliminarCampista),
    path('editarCampista/<idCam>',views.editarCampista),
    path('procesarEdicionCampista/',views.procesarEdicionCampista),

    path('listadoReserva/',views.listadoReserva),
    path('nuevoReserva/',views.nuevoReserva),
    path('guardarReserva/',views.guardarReserva),
    path('eliminarReserva/<idRes>',views.eliminarReserva),
    path('editarReserva/<idRes>',views.editarReserva),
    path('procesarEdicionReserva/',views.procesarEdicionReserva),
]