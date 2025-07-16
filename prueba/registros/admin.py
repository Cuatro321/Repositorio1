from django.contrib import admin
from .models import Alumnos, Comentario, ComentarioContacto

# Admin de Alumnos
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            return ('created', 'updated', 'matricula', 'carrera', 'turno')
        return ('created', 'updated')

admin.site.register(Alumnos, AdministrarModelo)


# Admin de Comentario con restricción para el grupo Admin1
class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'

  
    def alumno_solo_texto(self, obj):
        return obj.alumno.nombre
    alumno_solo_texto.short_description = "Alumno"

    def get_readonly_fields(self, request, obj=None):
        campos = ['created', 'id']
        if request.user.groups.filter(name="Admin1").exists():
            campos.append('alumno_solo_texto')  
        else:
            pass
        return campos

    def get_fields(self, request, obj=None):
        campos = ['id', 'created', 'coment']
        if request.user.groups.filter(name="Admin1").exists():
            campos.insert(2, 'alumno_solo_texto')  
        else:
            campos.insert(2, 'alumno')  
        return campos

admin.site.register(Comentario, AdministrarComentarios)

# class AdministrarComentarios(admin.ModelAdmin):
#     list_display = ('id', 'coment')
#     search_fields = ('id', 'created')
#     date_hierarchy = 'created'

#     def get_readonly_fields(self, request, obj=None):
#         if request.user.groups.filter(name="Admin1").exists():
#             return ('created', 'id', 'alumno') 
#         return ('created', 'id')

# admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje', 'created')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
