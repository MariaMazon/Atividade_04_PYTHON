 ### QUESTÃO 1

class Livro:
    livros=[]
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo=titulo
        self.autor=autor
        self.ano_publicacao=ano_publicacao
        self.disponivel=True
        
        Livro.livros.append(self)

### QUESTÃO 2
    def __str__(self):
        return f'{self.titulo} | {self.autor} | {self.ano_publicacao}'
    
    def listar_livros():
        for livro in Livro.livros:
            print(f'{livro.titulo.ljust(25)} | {livro.autor.ljust(25)} | {livro.ano_publicacao} ')
    
    
# livro1=Livro('Sítio do picapau amarelo','Monteiro Lobato','2001')
# livro2=Livro('O saci','Monteiro Lobato','1921')

# Livro.listar_livros()

### QUESTÃO 3

    #metodo de objeto
    def emprestar(self):
        self.disponivel=False
        
      
# livro3=Livro('Reinações de Narizinho','Monteiro Lobato',1931)  
# print(f'Antes de emprestar:  O livro está disponível? {livro3.disponivel}')
# livro3.emprestar()
# print(f'Depois de emprestar:  O livro está disponível? {livro3.disponivel}')

### QUESTÃO 4

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis=[livro for livro in Livro.livros if livro.ano_publicacao==ano and livro.disponivel]
        for livro in livros_disponiveis:
            print(f'Livros disponiveis em {ano}: {livro}')
        return livros_disponiveis

# livro1=Livro('Sítio do picapau amarelo','Monteiro Lobato','2001')
# livro2=Livro('O saci','Monteiro Lobato','1921')

# Livro.livros[livro1,livro2]

### QUESTÃO 5 e 6
# No arquivo biblioteca.py, empreste o livro
# chamando o método emprestar e imprima
# se o livro está disponível ou não após o
# empréstimo.
