from django.shortcuts import render
from .models import Ficha, Elemento, Fotografia
# Create your views here.

def home(request):
    fotografias = Fotografia.objects.all()
    for i in fotografias:
        print(i.fotografia.url)
    return render(request,'index.html',context={'fotografias':fotografias})

def mainmenu(request):
    principal = Elemento.objects.all()
    context = {'principal':principal}

    return render(request,'menu.html',context)

def show(request, pk):
    context = {}
    fotografias = Fotografia.objects.select_related('id_ficha').filter(id_ficha__id_elemento=pk)
    for i in fotografias:
        print(i)
    context['elemento'] = fotografias
    #context['pk']= int(pk)
    return render(request,'content.html', context=context)
