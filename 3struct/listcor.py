# Listas loop
 # Armazenar mais de uma informação
 # Manter a sequência dos dados em uma variavel

cor_cliente = input('Digite a cor desejada ')
cores = ['amarelo', 'verde', 'azul','vermelho']

if cor_cliente.lower() in cores:
    print('Temos está cor em estoque')
else:
    print('Não tem no estoque está cor no momento')