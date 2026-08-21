# Definindo classe

class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imc(self):
        return self.peso / self.altura **2

    def apresentar(self):
        return f"{self.nome} - {self.peso} - {self.altura} - {self.imc()}"

###############################################################################

#Criando o Objeto

p1 = Pessoa("Luan", 60, 2)
p2 = Pessoa("João", 60, 2)
p3 = Pessoa("Flávia", 60, 2)
p4 = Pessoa("Kevin", 60, 2)
p5 = Pessoa("Francisco", 60, 2)

# Lista dos objetos

lista_pessoas = [p1, p2, p3, p4, p5]

#Impressão em repetição com todos os objetos da lista_pessoas

for p in lista_pessoas:
    print(p.apresentar())

###############################################################################

# Transformando em dataframe

dados = [{"nome": p.nome, "peso": p.peso, "altura": p.altura, "imc": p.imc()} for p in lista_pessoas]

# Impressão apenas dos valores da lista

print(dados)

#Importação do panda

import pandas as pd

dados = pd.DataFrame(dados)

# Impressão tabela

print(dados)

dados['soma_peso_altura'] = dados['peso'] + dados['altura']
