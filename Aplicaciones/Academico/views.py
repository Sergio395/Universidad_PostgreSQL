from django.shortcuts import render
#from django.http import HttpResponse
from .models import Curso

# Create your views here.
def home(request):
    #return HttpResponse('<h1>CRUD en PostgreSQL</h1>')
    cursosListados=Curso.objects.all()
    return render(request,'gestionCursos.html',{"cursos": cursosListados})
    