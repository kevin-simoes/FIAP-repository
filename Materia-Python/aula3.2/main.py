#Ex.1
nome_1, idade_1 = "Ana", 25

def apresentar(nome, idade):
    print(f'Olá meu nome é {nome}, e minha idade é {idade} anos')

apresentar(nome_1, idade_1)

#Ex.2
class Pilha:
    def __init__(self):
        self.itens = [] # Cria pilha vazia
    def push(self, item):
        self.itens.append(item) # Adiciona no topo
    def pop(self):
        return self.itens.pop() # Remove do topo

# Uso
p = Pilha() # Cria um objeto na classe Pilha
p.push(10)

#Ex.3
class Bolo:
    def __init__(self, sabor):
        self.sabor = sabor

b1 = Bolo('Chocolate')
b2 = Bolo('Cenoura')

print(b1.sabor)

#Ex.4
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome #dado
        self.idade = idade #dado

    def fala(self):   # comportamento
        return f'Olá! Sou {self.nome}, tenho {self.idade} anos.'

p1 = Pessoa('Pedro', 18)
p2 = Pessoa('Carlos', 30)

print(p1.fala())      #Olá! Sou Pedro, tenho 18 anos.
print(p2.fala())      #Olá! Sou Carlos, tenho 30 anos.

#exercicio 1

class Aluno():
    def __init__(self, nome, curso, faculdade, semestre):
        self.nome = nome
        self.curso = curso
        self.faculdade = faculdade
        self.semestre = semestre

    def apresentar(self):
        return f'Olá, sou {self.nome}, faço o curso de {self.curso} na faculdade {self.faculdade}. Atualmente estou no {self.semestre}º'


# Objetos
p1 = Aluno("Kevin", "Engenharia de Software", "FIAP", 2)
p2 = Aluno("Gustavo", "Engenharia Elétrica", "FEI", 4)

print(p1.apresentar())

#exercicio 2

class Triangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return f'A área do triângulo é {self.base * self.altura}.'
    def perimetro(self):
        return f'O perimetro do triângulo é {self.base + self.altura}.'

t1 = Triangulo(5, 5)
t2 = Triangulo(10, 7)

print(t1.area())
print(t1.perimetro())