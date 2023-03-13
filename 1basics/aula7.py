

# == While Loops ==
# Excelente par loops dependentes de uma condição.
# Criar uma promoção para produto no valor de R$ 100,00

valor = 100
dia = 0
while valor > 10:
    dia += 1
    print(f' No dia {dia} o produto será vendido por R${valor}')
    valor -= 5