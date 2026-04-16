# Solicite dois números diferentes ao usuário (caso os números sejam iguais, o algoritmo deve solicitar os números novamente) e informe a soma entre os números.

while True:         # Loop infinito
    numero1 = int(input("Informe a idade: "))
    numero2 = int(input("Informe a idade: "))
    if numero1 != numero2:
        print(numero1+numero2)
        break       # Finaliza o loop