# Exercício 02
# Crie um dicionário conta com titular e saldo. Peça
# um valor de saque; se maior que o saldo, imprima
# 'Saldo insuficiente'.

conta = {'nome':'Luan',
         'saldo':18,
         }
conta['saque'] = int(input('Digite o valor do saque: '))

if conta['saldo'] >= conta['saque']:
    conta['saldo'] -= conta['saque']
    print(f'Saque de {conta['nome']} feito com sucesso, saldo restante: {conta["saldo"]}')
else:
    print(f'Saque é maior que o saldo atual: {conta["saldo"]}')
