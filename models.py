from django.db import models

class EstudianteBaile(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    estilo_preferido = models.CharField(max_length=50)
    nivel_experiencia = models.CharField(max_length=50)
    fecha_inscripcion = models.DateField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class InstructorBaile(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    estilo_especialidad = models.CharField(max_length=50)
    experiencia_anos = models.IntegerField()
    fecha_contratacion = models.DateField()
    salario_hora = models.DecimalField(max_digits=5, decimal_places=2)
    disponibilidad = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class EstiloBaile(models.Model):
    nombre_estilo = models.CharField(max_length=50)
    descripcion = models.TextField()
    origen = models.CharField(max_length=50)
    popularidad = models.IntegerField()
    musica_asociada = models.TextField()
    es_pareja = models.BooleanField()

    def __str__(self):
        return self.nombre_estilo


class ClaseBaile(models.Model):
    nombre_clase = models.CharField(max_length=100)
    instructor = models.ForeignKey(InstructorBaile, on_delete=models.CASCADE)
    estilo = models.ForeignKey(EstiloBaile, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=50)
    duracion_minutos = models.IntegerField()
    horario = models.CharField(max_length=100)
    cupo_maximo = models.IntegerField()
    costo_clase = models.DecimalField(max_digits=10, decimal_places=2)
    sala = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_clase


class InscripcionClaseBaile(models.Model):
    estudiante = models.ForeignKey(EstudianteBaile, on_delete=models.CASCADE)
    clase = models.ForeignKey(ClaseBaile, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado_inscripcion = models.CharField(max_length=50)
    fecha_finalizacion = models.DateField()
    comentarios_instructor = models.TextField()
    pago_realizado = models.BooleanField()

    def __str__(self):
        return f"Inscripción {self.id} - {self.estudiante}"


class EventoBaile(models.Model):
    nombre_evento = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_evento = models.DateField()
    hora_evento = models.TimeField()
    lugar = models.CharField(max_length=255)
    costo_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_evento = models.CharField(max_length=50)
    organizador = models.CharField(max_length=100)
    invitados_especiales = models.TextField()

    def __str__(self):
        return self.nombre_evento


class ParticipacionEventoBaile(models.Model):
    estudiante = models.ForeignKey(EstudianteBaile, on_delete=models.CASCADE)
    evento = models.ForeignKey(EventoBaile, on_delete=models.CASCADE)
    rol_participante = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField()
    calificacion_desempeno = models.DecimalField(max_digits=4, decimal_places=2)
    comentarios_organizador = models.TextField()

    def __str__(self):
        return f"{self.estudiante} en {self.evento}"
