# Function
    # DRY - Don´t report yourself

def boas_vindas(nome, quantidade):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} notbooks em estoque')

boas_vindas('Marcos', 5)
boas_vindas('Robert', 4)
boas_vindas('Linda', 3)
