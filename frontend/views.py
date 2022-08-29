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
    context = DIC
    context['pk'] = pk
    for i in range(1,194):
        if int(pk) == i:
            context['ruta_imagen'] = f'img/{i}.jpg'
            break
    
    return render(request,'menu.html', context=context)
