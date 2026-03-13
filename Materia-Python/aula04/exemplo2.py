"""

Exemplo de
comentário
com
várias linhas

"""

nome = input("Informe seu nome: ")                  # solicita o nome
idade = int(input("Informe sua idade: "))           # solicita a idade
altura = float(input("Infome sua altura: "))        # solicita a altura

print("Seu nome é",nome,"Sua idade é de", idade,"anos")
print(f"O seu nome é {nome} e sua idade é de {idade} anos")     # string
print("O seu nome é {} e sua idade é de {} anos".format(nome,idade))

print(f"O seu nome é{nome}")
print(f"A sua idade é de{idade} anos") # Método de pular linha manualmente
print(f"A sua altura é{altura} metros")

print(f"O seu nome é {nome}\nA sua idade é {idade}\nA sua altura é {altura}") # Método de pular usando \n