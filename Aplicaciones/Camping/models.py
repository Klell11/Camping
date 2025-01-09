from django.db import models

# Create your models here.
class Campista(models.Model):
    idCam = models.AutoField(primary_key=True)
    nombreCampista = models.CharField(max_length=250)
    correoCampista = models.EmailField()
    telefonoCampista = models.CharField(max_length=10)
    direccionCampista = models.TextField()

    def __str__(self):
        return self.nombreCampista


class Reserva(models.Model):
    idRes = models.AutoField(primary_key=True)
    fechaInicio = models.DateField()
    fechaFinal = models.DateField()
    tipoAlojamiento = models.CharField(max_length=250)
    numeroPersona = models.CharField(max_length=250)
    estadoReserva = models.CharField(max_length=250)
    observacionReserva = models.TextField(max_length=250)

    # Clave foránea hacia Campista con un related_name único
    campista = models.ForeignKey('Campista', on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva {self.idRes} - {self.campista.nombreCampista}"
    