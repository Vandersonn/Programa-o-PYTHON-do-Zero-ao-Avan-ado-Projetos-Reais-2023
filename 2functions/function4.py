# Function
    # DRY - Don´t report yourself
    # Parametro --> Argumento
    # Default = Aquele que você define o valor no parametro
    # Non-default = Aqquele que você não define o valor no parametro


def boas_vindas(nome, quantidade):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} notbooks em estoque')

boas_vindas('Marcos', 5)

