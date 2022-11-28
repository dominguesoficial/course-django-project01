from django.urls import path

from recipes.views import (  # As importações sempre ocorre da raiz. Logo, recipes e views é o caminho
    contato, home, sobre)

urlpatterns = [
    path("", home), 
    path("sobre/", sobre), 
    path("contato/", contato), 
]
