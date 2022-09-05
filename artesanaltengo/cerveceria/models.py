from django.db import models

# Create your models here.
class Marca(models.Model):
	nombre = models.CharField(max_length=60)
	direccion = models.CharField(max_length=60)
	#email = models.EmailField(blank=True, verbose_name='correo electrónico')
	
	def __str__(self):
		return self.nombre


	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Marcas"



class Cerveza(models.Model):
	precio = models.FloatField()
	cantidad = models.IntegerField()
	variedad = models.CharField(max_length=60)
	nombre = models.CharField(max_length=60)
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='imagenes')

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Cervezas"

	def __str__(self):
		return self.nombre
