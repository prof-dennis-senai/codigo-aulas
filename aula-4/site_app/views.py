from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "site_app/global/home.html")


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