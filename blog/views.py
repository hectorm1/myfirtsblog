from django.shortcuts import render
from .models import Articulo
from django .utils import timezone

# Create your views here.
def listar_publicaciones(request):
    publicaciones = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_publicaciones.html', {'publicaciones':publicaciones})
