# Enviar E-mail com detalhes da compra online(maximo 3)
# Tentativas para compra confirmada

compra_confirmada = False
dados_compra = 'Compra no valor de R$ 12,50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para o seu e-mail')
        break
else:
    print("falha na compra")
