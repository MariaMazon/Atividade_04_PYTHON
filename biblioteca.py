# QUESTÃO 5
from modelos.livro import Livro

# QUESTÃO 6
# livro_biblioteca=Livro('O saci','Monteiro Lobato',1921)
# print(f'Livro: {livro_biblioteca.disponivel}')
# livro_biblioteca.emprestar()
# print(f'Livro: {livro_biblioteca.disponivel}')

# QUESTÃO 7
ano_especifico=1921
Livro.verificar_disponibilidade(ano_especifico)