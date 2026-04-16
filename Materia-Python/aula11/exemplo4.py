# Solicitar a idade de N pessoas e calcular a média das idades
# finalizar a entrada de dados quando o usuário indicar uma idade negativa

cont = 0
soma = 0

while True:         # Loop infinito
    idade = int(input("Informe a idade: "))
    if idade < 0:
        break       # Finaliza o loop
    soma += idade
    cont += 1

media = soma / cont
print(f"Média das idades: {media}")