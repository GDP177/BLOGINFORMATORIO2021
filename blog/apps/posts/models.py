from django.db import models
from django.utils import timezone

class Post(models.Model):

	titulo = models.CharField(max_length=500)
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name =("Post")
		verbose_name_plural =("Posts")

class Comentario(models.Model):

		post = models.ForeignKey(Post, on_delete= models.CASCADE)
		contenido = models.TextField(max_length=500)
		#autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
		fecha_hora = models.DateTimeField(default=timezone.now)

		def __str__(self):
			return self.contenido

		class Meta:
			verbose_name = ("Comentario")
			verbose_name_plural = ("Comentarios")