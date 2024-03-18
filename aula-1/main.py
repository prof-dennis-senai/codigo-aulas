# snack_case
# nome_da_variavel = 35

# n1,n2 = (10,7),(5,6)

# print(n1,n2)

# nome = "Dennis" if nome_da_variavel < 35 else "Pedro"
# print(nome)


# if (condicao) :
#     ...  
idade = 15

#snake_case
def nome_funcao(idade, par2 = 0):
    idade += par2
    if idade >= 0:
        if idade > 18:
            print("você é maior de idade")
            
        elif idade >= 12:   
                print("Você é adolescente")
                
        else:
            print("Você é uma criança")
            
    else:
        print("Não é permitida a entrada de valores negativos")
        
    
    return idade >= 12 , idade
         
# n1,n2 = nome_funcao(idade)
# print(n1,n2)


def func1():
     print("func1")

def func2():
     print("func2")

def func3():
     print("func3")

def outrooo():
     print("Outroo")
x = 45   
nomes = {
    x > 30:func3, 
    x > 20:func2,
    x > 10:func1,
}

# nomes.get(True)()

# while idade < 9:
#     print("No ano de: 200" + str(idade), "o marcelo tem:", idade )
#     idade += 1
# else:
#     print("No ano de: 200" +  str(idade) + ".", "Qual a idade do marcelo?" )
    
# for i in range(1,11): 
#     if i == 5:
#         continue
#     print(i)
# else:
#     print("você é maior de idade")




########################################################

#1 nome class (abstração)
#2 caracteristicas (Atributos)
#3 O QUE VAI FAZER (Metodos)
#4 Sua caracteristica (Objetos)

""" 
Classe Carro

--- Caracteristicas (Atributos)
    marca
    modelo
    cor
    ano
    se tem rodas

--- O que faz? (Metodos)
    andar
    freia
    dar ré

---- Objetos
    carro1 (
    marca fiat
    modelo toro
    cor vermelha
    ano 2024
    tem rodas SIM
)

carro2 (
marca chevrolet
modelo onix
cor branco
ano 2020
se tem rodas SIM
)
"""



#PascalCase
class Pessoa:
    tamanho = 5

    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    

    @classmethod
    def func_static(cls,n1=0):
        print("antes:",cls.tamanho)
        cls.tamanho += n1
        print("depois:",cls.tamanho)


    def func_normal(self):
        print(">",self.tamanho)
        print("Normal")



pessoa1 = Pessoa("Dennis",26,1.7)
pessoa1.func_static(10)
pessoa1.func_normal()
print("-"*50)
Pessoa.func_static()
print("-"*50)
pessoa2 = Pessoa.func_static(22)

pessoa1.func_normal()





