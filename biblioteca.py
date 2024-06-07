from modelos.atividade_04 import Livro


livro4=Livro('Memórias da Emília', ' Monteiro Lobato', 1936)

print(f'Livro: {livro4.disponivel}')
livro4.emprestar()
print(f'Livro: {livro4.disponivel}')