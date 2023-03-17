from datetime import datetime
# Python Objected Oriented Programing

# Classes
    # Utiizadas para criar objetos (instances)
    # Objetos são parted dentro de uma class (instancias)
    # Classes são utilizadas par agrupar dados e funções,
    # podendo utilizar :
    # =====
    # class: frutas
    # Objects: Abacate, Banana....

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self. ano_nascimento = ano_nascimento

    def nome_completo(self):
        return (self.nome + '' + self.sobrenome)

    def idade_funcionario(self):
        ano_atual =  datetime.now().year
        self.ano_nascimento = int(ano_atual) - self.ano_nascimento
        return self.ano_nascimento


# objetos
user1 = Funcionarios('Eleina', 'Cabrasta', 1979)
user2 = Funcionarios('Carlos', 'Silva', 2001)
user3 = Funcionarios('Amasias', 'Asker', 1999)

# Print
print(Funcionarios.idade_funcionario(user1))

