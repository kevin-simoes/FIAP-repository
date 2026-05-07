# ------------------------------------------------------------------------------
# LISTA

# Armazena uma coleção de itens, organizados sequencialmente.
# Os itens são delimitados por colchetes [ ] e separados por vírgulas.
numeros = [5, 6, 20, 10, 3, 25]
print(numeros)

nomes = ['Ana', 'Paulo', 'João', 'Fernando', 'Marcela']
print(nomes)

# Listas são estruturas heterogêneas (armazenam dados de tipos diferentes)
lista = [1, 4, 5.99, 5.23, 'Ana', 'Paulo', True, False, 1]
print(lista)

# Lista vazia
lista = []
print(lista)

# Índices: representam a posição de cada item.
# O primeiro item sempre é zero.
# São utilizados para acessar um item específico da lista.
lista = [3, 6, 19, 89]
print(lista[2])
print(lista[0])
soma = lista[0] + lista[2]
print(soma)

# Índices negativos: acessam a lista a partir do último item.
# O último item sempre é -1.
lista = [3, 6, 19, 89, 10, 10, 10, 10, 10]
print(lista[-1])
print(lista[-2])
print(lista[-3])

# -----------------------------------------------------------
# inserir item no final da lista
lista = [2, 6, 10, 67, 10]
lista.append(50)
print(lista)
lista.append(60)
print(lista)

# inserir item em um indice especifico
lista.insert(0, 100)
print(lista)
lista.insert(3, 200)
print(lista)

# excluir item do final da lista
lista.pop()
print(lista)

# excluir item de um indice especifico
lista.pop(2)
print(lista)

# excluir a primeira ocorrencia de um valor da lista
lista.remove(10)
print(lista)

while 10 in lista:
    lista.remove(10)
print(lista)

while len(lista) > 0:
    lista.pop()
print(lista)

# -----------------------------------------------------------
# preencher a lista com entradas do usuário

# quantidade de itens pré-definida
lista = []
for cont in range(5):
    numero = int(input("Numero: "))
    lista.append(numero)
print(lista)

# quantidade indeterminada de itens
lista = []
while True:
    numero = int(input("Numero: "))
    if numero < 0:
        break
    lista.append(numero)
print(lista)

# ---------------------------------------------------
# perccorer os itens da lista
lista = [4, 6, 7, 8, 10, 66, 8]
for item in lista:
    print(item)

# contar quantos numeros pares estão na lista
cont = 0
for item in lista:
    if item % 2 == 0:
        cont += 1
print(f'Quantidade de pares: {cont}')

# percorrer os índices da lista
for i in range(len(lista)):        # 0,1,2,3,4,5,6
    print(lista[i])

# alterar os numeros pares para zero
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
print(lista)


