
# Set
    # Similar as listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 80]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union
print(num1 - num2) # diferente
print(num1 ^ num2) # simetric diferente
print(num1 & num2) # And

print(len(num1))

