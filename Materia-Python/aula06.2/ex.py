#exercicio 1###############################################################
numero =  lambda n: "Positivo" if n > 0 else "Negativo"
print(numero(-5))

#exercicio 2###############################################################

anos_de_vida = lambda idade: "Idoso" if idade > 60 else("Adulto" if idade >= 18 else("Adolescente" if idade >= 12 else "Criança"))
print(anos_de_vida(12))

#exercicio 3###############################################################

palavras = [("casa","azul"),("carro","vermelho"),("bicicleta","amarela")]

palavras_ordenadas1 = sorted(palavras, key=lambda x: x[0])
palavras_ordenadas2 = sorted(palavras, key=lambda x: x[1])
print(palavras_ordenadas1)
print(palavras_ordenadas2)

#exercicio 4###############################################################

palavras = [("casa","azul"),("carro","vermelho"),("bicicleta","amarela")]

lista_ord_comprimento = sorted(palavras, key=lambda x: len(x[1]))
print(lista_ord_comprimento)