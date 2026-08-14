livro = {}
livro['nome'] = input('Digite o nome do livro que está lendo: ')
livro['paginas'] = int(input('Digite a quantidade de páginas do livro: '))
livro['paginas lidas'] = int(input('Digite a quantidade de páginas que leu: '))

percentual = livro['paginas'] - livro['paginas lidas']
# Tem que achar a resposta
print(percentual)