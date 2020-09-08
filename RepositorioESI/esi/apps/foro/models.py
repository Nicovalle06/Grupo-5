from django.db import models

# Create your models here.
class Foro(models.Model):
    topico =  models.CharField(max_length = 255)
    post = models.TextField(null = True)
    comentario = models.TextField(null = True)
    usuario = models.CharField(max_length = 80)

class Usuario(models.Model):
    nombre =  models.CharField(max_length = 80)
    email = models.EmailField(max_length=254, primary_key = True)



'''
class Blog(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Entrada(models.Model):
    blog = models.ForeignKey(Blog)
    encabezado = models.CharField(max_length=255)
    cuerpo_texto = models.TextField()
    fecha_public = models.DateTimeField()
    autores = models.ManyToManyField(Autor)
    def __str__(self):
        return self.headline

'''
'''
class Rubro(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	codigo = models.CharField(max_length = 15, primary_key = True)
	nombre = models.CharField(max_length = 80)
	descripcion = models.TextField(null = True)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	oferta = models.BooleanField()
	imagen = models.ImageField(upload_to="productos",null = True,blank=True)
	rubro = models.ForeignKey(Rubro,related_name = 'mirubro', null=True, on_delete = models.SET_NULL)
	def __str__(self):
		return self.nombre

'''
