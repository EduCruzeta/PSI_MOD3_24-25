"""
1. Uma função que recebe dois parâmetros. 
A função deve calcular e mostrar a soma de todos os números inteiros entre dois parâmetros, inclusive
"""

def Somar(x1,x2):
    soma = 0
    for x in range (x1,x2+1):
        soma = soma + x
    print(soma)

# Exemplos 3 e 5 = 3 + 4 + 5 = 12

Somar(3,5)