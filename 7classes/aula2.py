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
    pass

#objeto
user1 = Funcionarios()
user2 = Funcionarios()

#parametros do 1 user
user1.nome = 'Elena'
user1.sobrenome = 'Cabral'
user1.data_nascimento = '20/08/2001'

#parametros do 2 user
user2.nome = 'Nena'
user2.sobrenome = 'Carvalho'
user2.data_nascimento = '30/10/2009'

#print
print(user1.nome)
print(user2.nome)
print(user1.data_nascimento)