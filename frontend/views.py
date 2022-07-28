from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html',context={})

def mainmenu(request):
    return render(request,'menu.html',context={})
