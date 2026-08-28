#Função com lambda
from pip._internal.cli import base_command

soma = lambda x, y: x + y
print(soma(4, 5))

#Função com def
def soma(x, y):
    resultado = x + y
    return resultado
print(soma(4, 5))

lista = [100,90,80,50,85,73,53]
lista.sort()
lista.sort(reverse=True)
print(lista)

lista_ordenada = sorted(lista)
lista_ordenada = sorted(lista, reverse=True)

lista_frutas = [('uva',10),('laranja',5),('banada',3)]

lista_ordenada=sorted(lista_frutas, key=lambda x: x[1])
print(lista_ordenada)

####################################################################

resultado = lambda palavra1, palavra2: palavra1 + " " + palavra2
print(resultado("Bom","Dia"))

