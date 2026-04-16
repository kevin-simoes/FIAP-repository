# Escreva um algoritmo que solicite 10 números e informe qual foi o menor número digitado.

cont = 0
cont_pares = 0
cont_impares = 0
num_pares = 0
num_impares = 0
while cont < 10:
    numero = int(input("Numero: "))
    if numero % 2 == 0:
        num_pares += numero
        cont_pares += 1
    if numero % 2 != 0:
        num_impares += numero
        cont_impares += 1
    cont += 1

print(f"")