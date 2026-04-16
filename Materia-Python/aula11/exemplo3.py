# Solicitar a idade de 10 pessoas e calcular a média das idades

soma = 0                    # varíavel contadora
cont = 0                    # variável somadora

while cont < 10:
    idade = int(input("Informe uma idade: "))
    soma += idade           # realiza o somatório das idades
    cont += 1

media = soma / 10
print (f'Média das idade: {media:.2f}')

