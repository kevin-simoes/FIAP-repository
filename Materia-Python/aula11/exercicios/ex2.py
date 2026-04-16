# 2. Escreva um algoritmo que solicite a idade de 10 pessoas e
# informe a quantidade de pessoas com idade inferior a 18 anos.

cont = 0
dmenor = 0
while cont < 10:
    numero = int(input("Numero: "))
    if numero < 18:
        dmenor += 1
    cont += 1

print(f"De {cont}, {dmenor} são menores de idade")