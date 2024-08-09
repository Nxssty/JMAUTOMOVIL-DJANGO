from django.db import models

class Autos(models.Model):

    BENCINERO = 'Bencinero'
    DIESEL = 'Diesel'
    ELECTRICO = 'Electrico'
    HIBRIDO = 'Hibrido'
    GAS_NATURAL = 'Gas Natural'
    HIDROGENO = 'Hidrogeno'
    COMBUSTIBLE_CHOICES = [
        (BENCINERO, 'Bencinero'),
        (DIESEL, 'Diesel'),
        (ELECTRICO, 'Electrico'),
        (HIBRIDO, 'Hibrido'),
        (GAS_NATURAL, 'Gas Natural'),
        (HIDROGENO, 'Hidrogeno'),
    ]

    AUTOMATICO = 'Automático'
    MANUAL = 'Manual'
    TRANSMISION_CHOICES = [
        (AUTOMATICO, 'Automático'),
        (MANUAL, 'Manual'),
    ]


    marca = models.CharField(max_length=50, verbose_name='Marca', help_text='Primera letra en Mayusculas')
    modelo = models.CharField(max_length=50, verbose_name='Modelo', help_text='Primera letra en Mayusculas')
    cilindrada = models.CharField(max_length=5, verbose_name='Cilindrada', help_text='Ejemplo: 2.0')
    anio = models.CharField(max_length=5, verbose_name='Año', help_text='Solo poner el año: Ejemplo: 2013')
    transmision = models.CharField(max_length=20, choices=TRANSMISION_CHOICES, default=MANUAL, verbose_name='Transmisión')
    kilometraje = models.CharField(max_length=20, verbose_name='Kilometraje', help_text='Ejemplo: 144.000')
    combustible = models.CharField(max_length=20, choices=COMBUSTIBLE_CHOICES, default=BENCINERO, verbose_name='Combustible')
    descripcion = models.CharField(max_length=1000, verbose_name='Descripción', help_text='Descripción breve del vehículo!')
    precio = models.CharField(max_length=20, verbose_name='Precio', help_text='Ejemplo: 234.000')
    vendido = models.BooleanField(default=False, verbose_name='Vendido')
    recien_llegado = models.BooleanField(default=True, verbose_name='Recién Llegado')


    def __str__(self):
            return self.marca+" "+self.modelo
    
class Imagen(models.Model):
    auto = models.ForeignKey(Autos, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='autos/')

    def __str__(self):
        imagen_numero = self.auto.imagenes.filter(id__lte=self.id).count()
        return f"{self.auto} - Imagen {imagen_numero}"