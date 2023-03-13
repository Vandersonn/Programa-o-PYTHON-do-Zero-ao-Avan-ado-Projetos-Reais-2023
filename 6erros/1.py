# Erros
    # Excelente para testes
    # Não realiza o estope no progrma
    # Mensagens cistomizadas quando encontra um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Página não existe')


