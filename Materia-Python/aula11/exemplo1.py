# Validação de entrada do usuário
# Solicitar a nota de um aluno (0 - 10)

nota = float(input("Informe a nota: "))
while nota < 0 or nota > 10:
    nota = float(input("Nota inválida. Digite novamente: "))

print(f"A nota informada foi {nota}")