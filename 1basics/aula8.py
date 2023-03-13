

# == While Loops ==
# Excelente par loops dependentes de uma condição.
# Publicar um produto com comissaão de 10% se for acima de R$ 20,00

valor = float(input('Digite o valor do seu produto em R$ '))
dia = 0
while valor > 20:
    valor = (valor * 0.10) + valor
    print(f' No O valor final do seu produto será R${valor}')
    break