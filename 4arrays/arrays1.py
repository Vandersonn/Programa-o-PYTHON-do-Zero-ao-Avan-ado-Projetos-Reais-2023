from array import array
# Arrays
    # Array (Matriz)
    # Similar a lista com melhor perfomance

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40, 50]
numeros_f = [1.2, 2.2, 3.2, 4.2]

print(letras)
print(numeros_i)
print(numeros_f)

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40, 50])
numeros_f = array('f', [1.2, 2.2, 3.2, 4.2])
print(letras)
print(numeros_i)
print(numeros_f)