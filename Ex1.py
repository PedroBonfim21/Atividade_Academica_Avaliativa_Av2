'''
1. (0,5) Faça função que calcule a área do trapézio, dados:
a. Base maior
b. Base menor
c. Altura
Lembrando que a área pode ser calculada por: 𝑎𝑟𝑒𝑎 =
(𝑏𝑚𝑎𝑖𝑜𝑟 + 𝑏𝑚𝑒𝑛𝑜𝑟). 𝑎𝑙𝑡𝑢𝑟𝑎/2
O programa principal deve pedir os valores e usar a função para calcular a
área.
'''
def area():
    Bmaior=float(input('Digite um valor para a base maior do trapezio: '))
    Bmenor=float(input('Digite o valor da base menor do trapezio: '))
    Alt=float(input('Digite o valor da altura do trapezio: '))
    area=((Bmaior+Bmenor)*Alt)/2
    print(area)

area()