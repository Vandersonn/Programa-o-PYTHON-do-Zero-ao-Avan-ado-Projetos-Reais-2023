
# Dicionários
    # Utiliza index no formato das Keys e Values
    # Aceita Strings, Integer, Float, Boolean...

aluno = {'nome': 'Anna',
         'idade': 16, 'nota_final': 'A',
         'Aprovação': 'Sim',
         'Materias':['Fisica','Matemática', 'Geografia']}

print(aluno.get('Materias'))
print(len(aluno))
print(aluno.keys())
print(aluno.items())
print(aluno.values())