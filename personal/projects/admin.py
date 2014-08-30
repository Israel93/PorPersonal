from django.contrib import admin
from models import *


class ProjectAdmin(admin.ModelAdmin):
	list_display=('id','titulo','fecha','imagenProject',)
	list_editable=('titulo','fecha',)

class TeamAdmin(admin.ModelAdmin):
	list_display=('id','nombre','apellidos','correo',)
	list_editable=('nombre','apellidos','correo',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Project, ProjectAdmin)
