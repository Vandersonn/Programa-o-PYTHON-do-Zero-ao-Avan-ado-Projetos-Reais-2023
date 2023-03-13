# Erros
    # Excelente para testes
    # Não realiza o estope no progrma
    # Mensagens cistomizadas quando encontra um erro

try:
    valor = int(input('Digite o valor do seu produto: '))

    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')

finally:
    print('Código okay')
