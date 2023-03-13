# Filter Function
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, filtrando os items,
    # lists, tuple, dic e etc...

frutas = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
'''frutass = []

for itens in frutas:
    if 'o' in itens:
        frutass.append(itens)
'''
frutass = [iten for iten in frutas if 'n' in iten]
print(frutass)