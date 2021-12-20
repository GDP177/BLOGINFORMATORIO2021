from django.db import models
from django.utils import timezone
# Create your models here.
from apps.user.models import Usuario

class Noticia(models.Model):

	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.fecha_publicacion= timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name =("Noticia")
		verbose_name_plural =("Noticia")

class Comentario(models.Model):
	noticia = models.ForeignKey(Noticia, on_delete= models.CASCADE)
	contenido = models.TextField()
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	fecha_hora = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.contenido

	class Meta:
		verbose_name = ("Comentario")
		verbose_name_plural= ("Comentarios")