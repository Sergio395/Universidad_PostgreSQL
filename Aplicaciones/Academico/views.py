from django.shortcuts import render
#from django.http import HttpResponse
from .models import Curso

# Create your views here.
def home(request):
    #return HttpResponse('<h1>CRUD en PostgreSQL</h1>')
    
    # cursosListados=Curso.objects.all()
    # cursosListados=Curso.objects.all()[:5]
    # cursosListados=Curso.objects.all()[4:9]
    # cursosListados=Curso.objects.all().order_by('creditos','-nombre') #desc
    #cursosListados=Curso.objects.filter(nombre='Historia')
    #cursosListados=Curso.objects.filter(nombre__startswith='Q')
    cursosListados=Curso.objects.filter(nombre__contains='g')
    #cursosListados=Curso.objects.filter(creditos__gte=4) #__lte=4 es <=4
    return render(request,'gestionCursos.html',{"cursos": cursosListados})
    