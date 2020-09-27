from django.db import models
from django.utils import timezone
from django.conf import settings



# Create your models here.
class Verdad(models.Model):
    tematicas = (
        ('metodos_anticonceptivos', 'Metodos anticonceptivos'),
        ('masculinidades', 'Masculinidades'),
        ('relaciones_sexuales', 'Relaciones sexuales'),
        ('noviazgo', 'Noviazgo'),
        ('violencia', 'Violencia'),
        ('feminismo', "Feminismo"),
        ('ETS', 'Enfermedades de transmisión sexual'),
        ('ESI', 'Educación Sexual')
    )
    topic = models.CharField(max_length=30,
                  choices=tematicas,
                  default="feminismo")
    title = models.CharField(max_length=200)
    description = models.TextField()
    imagen = models.ImageField()
    verdad = models.TextField()
    mito = models.TextField()
    conclusion = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title





