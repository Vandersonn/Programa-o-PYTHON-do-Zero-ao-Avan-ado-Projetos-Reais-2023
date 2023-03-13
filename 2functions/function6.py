# Functions
    # DRY - Don´t report yourself
    # Realize uma tarefa
    # Vários Argumentos(xargs)

# Criar uma função que soma vários números

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2,4,8,10)
print(x)
