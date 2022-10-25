from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100,default='')
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha_de_nacimiento = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return f"Id: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Pasaporte: {self.numero_pasaporte}, Fecha nacimiento: {self.fecha_de_nacimiento}"

 
