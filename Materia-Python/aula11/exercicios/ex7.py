# Faça um algoritmo que solicite um número inteiro ao usuário e
# calcule o fatorial desse número. O fatorial de um número N é a multiplicação
# de N por seus antecessores maiores ou iguais a 1.
# Por exemplo: o fatorial de 5 é igual a 120 (5 * 4 * 3 * 2 * 1).

fatorial = 1

n = int(input("Digite um número: "))
cont = n

while cont >= 1:
    fatorial *= cont
    cont -= 1

print(f"{n}! = {fatorial}")


