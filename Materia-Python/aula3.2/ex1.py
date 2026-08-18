nome_1, idade_1 = "Ana", 25

def apresentar(nome, idade):
    print(f'Olá meu nome é {nome}, e minha idade é {idade} anos')

apresentar(nome_1, idade_1)

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

