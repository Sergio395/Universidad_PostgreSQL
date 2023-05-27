from django.contrib import admin
from .models import Curso
# Register your models here.

#1 admin.site.register(Curso)
@admin.register(Curso) #3
class CursoAdmin(admin.ModelAdmin): #2 y #3
    
    #ordering=('-nombre',) #tupla indicarlo con la coma
    #ordering=('creditos', 'nombre')
    search_fields=('nombre', 'creditos')
    #list_display=('id','nombre','creditos') #+columnas,sobrescribe __str__ de model
    #list_editable = ('nombre','creditos') #lista y edita(va con list_display)
    #list_display_links = ('nombre',)
    #list_filter =('creditos',)
    #list_per_page=3 #3 registros por pagina
    #exclude = ('creditos',) #desaparecen 
    
#2 admin.site.register(Curso, CursoAdmin)
