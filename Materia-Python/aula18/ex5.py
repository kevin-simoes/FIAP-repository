# Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada area
# que calcula e retorna a área do círculo e outra função chamada perimetro que calcula e retorna o
# perímetro do círculo. Utilize as fórmulas abaixo
# Área = π * r2
# Perímetro = π * 2 * r

def calculoArea(circulo):
    area = 3,14 * (circulo*circulo)
    return area

def calculoPerimetro(circulo):
    perimetro = 3,14 *( 2 * circulo)
    return perimetro

num = int(input("Digite o número do raio do círculo: "))

calculo_area = calculoArea(num)
calculo_perimetro = calculoPerimetro(num)

print(f"O valor da área do círculo é {calculo_area} e o perímetro é {calculo_perimetro}")
