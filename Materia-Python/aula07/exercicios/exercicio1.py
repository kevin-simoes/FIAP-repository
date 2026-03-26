nome = input("Digite o nome do aluno: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media >= 6:
    print(f"O aluno {nome} aprovado")
    print(f"Média: {media}")
elif media < 6:
    print(f"O aluno {nome} reprovado por média")
    print(f"Média: {media}")