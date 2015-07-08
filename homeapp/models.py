# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Autor(models.Model):
	''' Tabela de autores das postagens '''
	nome = models.CharField('Nome', max_length=100)
	formacao = models.CharField('Formação', max_length=200)
	email = models.EmailField('E-mail', max_length=50, unique=True)

	class Meta:
		verbose_name = "Autor"
		verbose_name_plural = "Autores"
	
	def __str__(self):
		return self.nome

class Post(models.Model):
	''' Tabela de armazenamento das postagem '''
	nome = models.ForeignKey(Autor, null=True)
	titulo = models.CharField('Título', max_length=200)
	texto = models.TextField()
	criado_data = models.DateTimeField('Criado em', default=timezone.now)
	publicado_data = models.DateTimeField('Publicado', blank=True, null=True)

	def publicar(self):
		self.publicado_data = timezone.now()
		self.save()

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posters"

	def __str__(self):
		return self.titulo