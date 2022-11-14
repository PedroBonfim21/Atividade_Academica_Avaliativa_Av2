'''
Faça um programa em Python com uma função chamada
somaImposto. A função possui dois parâmetros formais:
a. taxaImposto, que é a quantia de imposto sobre vendas expressa
em porcentagem; e
b. custo, que é o custo de um item antes do imposto. A função "altera" o
valor de custo para incluir o imposto sobre vendas.
O programa principal deve pedir os dados e usar a função para calcular preço
do produto.
'''
def somaImposto():
    taxaImposto=float(input('Digite a taxa de imposto sobre as vendas em %: '))
    custo=float(input('Digite o valor do produto: '))
    custo=((taxaImposto/100)*custo)+custo
    print(custo)

somaImposto()