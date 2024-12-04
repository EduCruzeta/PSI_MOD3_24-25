"""
2. Crie uma função que mostra a média de 5 valores.
A função deve ler os valores do utilizador e, posteriormente, calcular e mostrar a média dos valores.
"""

def Media():
    media = 0
    for i in range(5):
        numero = float(input("insira o valor: "))
        media = media + numero
    media = media / 5
    print(media)

# Exemplo 1 + 2 + 3 + 4 + 5 = 15 / 5 = media de 3

Media()