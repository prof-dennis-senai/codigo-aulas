from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "site_aula/home.html")

def sobre(request):
    dados = {
        'lista_titulo' : range(1,7)
    }
    return render(request, "site_aula/sobre.html",context=dados)


def contato(request):
    return render(request, "site_aula/contatos.html")