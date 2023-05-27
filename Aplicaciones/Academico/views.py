from django.shortcuts import render
from django.views.generic import ListView
#from django.http import HttpResponse
from .models import Curso

# Create your views here.
#----Vistas basadas en funciones------
def home(request):
    #return HttpResponse('<h1>CRUD en PostgreSQL</h1>')
    
    cursosListados=Curso.objects.all() #listado desde el ORM
    # cursosListados=Curso.objects.all()[:5]
    # cursosListados=Curso.objects.all()[4:9]
    # cursosListados=Curso.objects.all().order_by('creditos','-nombre') #desc
    #cursosListados=Curso.objects.filter(nombre='Historia')
    #cursosListados=Curso.objects.filter(nombre__startswith='Q')
    #cursosListados=Curso.objects.filter(nombre__contains='g')
    #cursosListados=Curso.objects.filter(creditos__gte=4) #__lte=4 es <=4
    data={ #Diccionario= permite enviar muchos datos diferentes al html
        'titulo':'Gestión de Mis Cursos', # En html borré el title
        'cursos': cursosListados
    }
    
    #return render(request,'gestionCursos.html',{"cursos": cursosListados})
    return render(request,'gestionCursos.html',data)
   
   #----Vistas basadas en Clases (Vistas basadas en Modelos)//Reemplaza a funcion home-------------
   
class CursoListView(ListView): #hay que registrarla en admin.py y agregar un urls.py en cada app
    model = Curso
    template_name = 'gestionCursos.html'
    
    def get_queryset(self):
        return Curso.objects.filter(creditos__lte=4) #sobrescribo queryset que viene x default
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Gestion de Cursos'
        print(context)
        return context  
       
       