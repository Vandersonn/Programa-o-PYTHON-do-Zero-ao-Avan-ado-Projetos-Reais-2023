# For loop nested
    # Outer loop
        # Inner loop
"""
Criar retangulo
@@@@
@@@@
@@@@
"""
linhas = 3
colunas = 5
simbolo = '@'

for l in range(linhas):
    for c in range(colunas + l):
        print(simbolo, end='')
    print()