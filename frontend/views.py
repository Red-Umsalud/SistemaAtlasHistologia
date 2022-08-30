from django.shortcuts import render
from .models import Ficha, Elemento, Fotografia
# Create your views here.

def home(request):
    return render(request,'index.html', {})

def mainmenu(request):
    principal = Elemento.objects.all()
    context = {'principal':principal}
    return render(request,'menu.html', context)

def show(request, pk):
    context = {}
    fotografias = Fotografia.objects.select_related('id_ficha').filter(id_ficha__id_elemento=pk)
    context['elemento'] = fotografias
    principal = Elemento.objects.all()
    context['principal'] = principal
    return render(request,'menu.html', context=context)
