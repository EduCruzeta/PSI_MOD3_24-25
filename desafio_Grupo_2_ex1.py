"""
1. Desenvolva uma função que recebe uma string e devolve verdadeiro 
se todas as letras da string são iguais e falso nos restantes casos.
"""

def Funcao1(palavra) -> str :
    letra_anterior = ""
    Temp = True
    for letra in palavra:
        if Temp == True:
            letra_anterior = letra
            Temp = False
        elif letra != letra_anterior:
            return False
        letra_anterior = letra
    return True

# se alguma letra for diferente a função vai devolver false caso for tudo igual devolve true