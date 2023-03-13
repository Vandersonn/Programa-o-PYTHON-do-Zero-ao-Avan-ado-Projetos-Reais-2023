from sys import getsizeof

# Generation Expression
    # Uma forma mais rapida pa listas, dic e etc...
    # Menos memória alocada
    # Valores em bytes

numeros = [x * 10 for x in range(10)]
print(type(numeros))
print(getsizeof(numeros))
print(numeros)

numeros = (x * 10 for x in range(10))
print(type(numeros))
print(getsizeof(numeros))
print(list(numeros))