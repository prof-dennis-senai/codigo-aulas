from django.shortcuts import render, redirect
from site_app.models import Pessoa


# Create your views here.
def home(request):
    datas = Pessoa.objects.all().order_by('-id')[:10]       
    return render(request, "site_app/partials/home.html", context={"dados":datas})

def pesquisar(request):
    datas = {}
    nome_filter = request.GET.get("nome")
    
    if nome_filter:
        datas["dados"] = Pessoa.objects.filter(nome__icontains=nome_filter)
    else:
        import ipdb; ipdb.set_trace()
        datas["dados"] = Pessoa.objects.all()

    return render(request, "site_app/partials/pesquisar.html", context={"dados":datas})

def criar(request):
    pessoa = {}

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        Pessoa.objects.create(nome=nome,email=email)
        pessoa = {
            "nome" : nome,
            "email" : email,
        }

    return render(request, "site_app/partials/criar.html", context=pessoa)

def deletar(request,id=0):
    datas = {}
    if id:
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()

    nome_filter = request.GET.get("nome")
    if nome_filter:
        datas["dados"] = Pessoa.objects.filter(nome__icontains=nome_filter)
    else:
        datas["dados"] = Pessoa.objects.all()
    
    return render(request, "site_app/partials/deletar.html", datas)

def atualizar(request,id=0):
    datas = {}
    if id:
        pessoa = Pessoa.objects.get(id=id)
        if not request.POST:
            return render(request, "site_app/partials/update.html", context={"pessoa":pessoa})
        
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        if nome:
            pessoa.nome = nome
        if email:
            pessoa.email = email

        pessoa.save() 

    nome_filter = request.GET.get("nome")
    
    if nome_filter:
        datas["dados"] = Pessoa.objects.filter(nome__icontains=nome_filter)
    else:
        datas["dados"] = Pessoa.objects.all()
    
    return render(request, "site_app/partials/atualizar.html", datas)



def produtos(request):
    return render(request, "site_app/global/produtos.html")

def precos(request, id=0):
    dados = [
        {
            "id":1,
            "titulo" : "X bacon",
            "descricao" : "Double Bacon, Dois super hamburgueres de 100g, queijo cheddar, cebola caramelizada",
            "img": "https://img.restaurantguru.com/r483-ItaGastroPub-burger-2021-09.jpg"
        },
        {
            "id":2,
            "titulo" : "X Galinha",
            "descricao" : "Dois super hamburgueres de Frango 100g, queijo Mussarela e tomate",
            "img": "https://imagens.jotaja.com/produtos/6dcc15bd-80cb-426f-acd7-2f52de6f75cb.jpg"
        },
        {
            "id":3,
            "titulo" : "Mafioso",
            "descricao" : "Dois super hamburgueres de 100g, queijo Mussarela, cebola caramelizada e Jack Daniels",
            "img": "https://img.restaurantguru.com/rcb4-burger-ItaGastroPub.jpg"
        },
    ]

    if id:
        # import ipdb; ipdb.set_trace()
        dados = [dados[id - 1]]
    return render(request, "site_app/global/precos.html", context={"dados":dados})