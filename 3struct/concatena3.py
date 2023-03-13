# Listas
 # Armazenar mais de uma informação
 # Manter a sequência dos dados em uma variavel

produtos = ['arroz', 'feijão', 'laranja', 'banana', 1, 3, 5]

item1, item2, item3, *outros = produtos

print(item1, item2)
print(produtos)