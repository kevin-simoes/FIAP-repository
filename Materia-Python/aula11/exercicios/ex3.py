# 3. Solicite vários números ao usuário (até que ele digite o número zero) e informe o somatório dos números digitados.

cont = 0
while True:         # Loop infinito
    numero = int(input("Informe a idade: "))
    if numero == 0:
        print(cont)
        break       # Finaliza o loop
    cont += 1