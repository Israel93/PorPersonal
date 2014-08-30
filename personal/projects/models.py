from django.db import models

#
#	Esta clase es para controlar los proyectos 
#	realizados 
#	- Faltan atributos
#	Link
#	Empresa para la que se desarrollo
#	Lenguaje de Programacion
#	Colaboradores	
#
class Team(models.Model):
	nombre 			= models.CharField(max_length=45)
	apellidos		= models.CharField(max_length=45)
	correo			= models.EmailField()
	sitio 			= models.URLField()

	def __unicode__(self):
		return self.nombre+" "+self.apellidos


class Project(models.Model):
	titulo 			= models.CharField(max_length=45)
	descripcion		= models.TextField(('Descripcion'), max_length=100)
	fecha 			= models.DateField(('Fecha'), auto_now_add=False)
	imagen 			= models.ImageField(upload_to='img')
	lenguaje 		= models.CharField(max_length=45)
	url 			= models.URLField()
	github			= models.URLField()
	colaborador 	= models.ManyToManyField(Team , null=True,blank=True)

	def __unicode__(self):
		return self.titulo

	def imagenProject(self):
		return """
		<img src="%s"/>
		"""%self.imagen.url
	imagenProject.allow_tags=True
	imagenProject.admin_order_field='imagen'

	def get_absolute_url(self):
		return '/project/%s/'%self.titulo+"#trabajo"

	def url_imagen(self):
		return self.imagen.url
	url_imagen.allow_tags = True
	url_imagen.admin_order_field="imagen"




# class Evento(models.Model):
#     titulo      = models.CharField(max_length = 45)
#     descripcipn = models.TextField(('Descripcion'), max_length = 45)
#     fechaevento = models.DateField(('Fecha de Evento'),auto_now_add=False)
#     hora        = models.TimeField(auto_now_add=False)
#     tipoevento  = models.ForeignKey(TipoEvento)
#     Promotor    = models.ForeignKey(Promotor)
#     costo       = models.FloatField()
#     destino     = models.ForeignKey(Destino)
#     activo      = models.BooleanField(default=True)
#     imagen      = models.ImageField(upload_to='img')

#     def __unicode__(self):
#       return self.titulo

#     def evento_imagen(self):
#       return """
#         <img src="%s" />
#       """%self.imagen.url
#     evento_imagen.allow_tags = True
#     evento_imagen.admin_order_field ='imagen'

#     def imagenevento(self):
#       return self.imagen.url
#     evento_imagen.allow_tags = True
#     evento_imagen.admin_order_field ='imagen'
    
#     def costoevento(self):
#       if self.costo == 0:
#         return 'Gratis'
#       else:
#         return "$ %s"%self.costo