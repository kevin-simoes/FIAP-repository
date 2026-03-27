salario = int(input('Digite o salário fixo: '))
vendas = int(input('Digite o valor das vendas: '))

comissao = vendas * 0.03

if comissao > 1500:
    p5 = vendas - 1500
    p3 = (vendas * 0.03) - p5
    comissao == (p5 * 0.05) + p3

total = comissao + salario

print(total)


