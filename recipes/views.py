from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Paulo Domingues',
        
    })


def contato(request):
    return HttpResponse('Contato OBS.: Para funcionar, 1° tenho que IMPORTAR no arquivo urls.py ')


def sobre(request):
    return HttpResponse('Sobre')




