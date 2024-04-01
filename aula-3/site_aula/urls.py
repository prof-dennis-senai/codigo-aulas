from django.urls import path
from site_aula.views import home, sobre,contato

urlpatterns = [
    path('', home),
    path('sobre-mim/', sobre),
    path('contatos/', contato),
]