from django.shortcuts import render
from .models import post 
from django .utils import timezone

# Create your views here.
def listar_publicaciones(request):
    publicaciones = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_publicaciones.html', {'publicaciones':publicaciones})
