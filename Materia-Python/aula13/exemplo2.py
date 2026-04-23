# Solicitar ao usuário 10 números e contar quantos números são pares e
# quantos números são impares

cont_pares = 0
cont_impares = 0

quantidade = int(input("Informe a quantidade de números: "))
for cont in range(quantidade):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

print(f'Quantidade de pares: {cont_pares}')
print(f'Quantidade de impares: {cont_impares}')