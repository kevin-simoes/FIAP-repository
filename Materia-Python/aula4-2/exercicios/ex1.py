# Exercício 01
# Peça nome e três notas de um aluno via input(),
# guarde em um dicionário, calcule a média e use if
# para imprimir 'Aprovado' ou 'Reprovado'.

aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno["nota1"] = int(input("Digite a nota 1 aluno: "))
aluno["nota2"] = int(input("Digite a nota 2 aluno: "))
aluno["nota3"] = int(input("Digite a nota 3 aluno: "))

aluno['media'] = (aluno["nota1"] + aluno["nota2"]+ aluno["nota3"])/3


if aluno['media'] > 6:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')