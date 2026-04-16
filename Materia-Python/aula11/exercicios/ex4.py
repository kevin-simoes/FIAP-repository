# Faça um algoritmo que solicite N números e calcule a média dos números pares e a média dos números ímpares (o valor de N deve ser solicitado ao usuário no início do programa).

n = int(input("Digite quantos números vai digitar: "))

cont = 0
cont_pares = 0
cont_impares = 0
num_pares = 0
num_impares = 0
while cont < n:
    numero = int(input("Numero: "))
    if numero % 2 == 0:
        num_pares += numero
        cont_pares += 1
    if numero % 2 != 0:
        num_impares += numero
        cont_impares += 1
    cont += 1

print(f"Dos {n} digitados, a média dos pares é {num_pares/cont_pares} e de impares é {num_impares/cont_impares}")