"""
Para cada letra do alfabeto português, indique o número de vezes que aparece na frase
Todos os caracteres que não pertencem ao alfabeto português não devem contabilizar.
"""
"""
Sugestão:
    utilizar as funções ord() e/ou chr() para pecorrer p alfabeto
    print(ord("a"))
    print(chr(97))
"""

def Contarletra (letra,frase):
    """ Função para contar quantas vezes a letra aparece na frase"""
    contar = 0
    for l in frase:
        if letra == l:
            contar = contar + 1
    return contar

def ContarFrequencia(frase):
    """Função que mostra o nº de vezes que cada letra do alfabeto aparece na frase"""
    # precorrer o alfabeto
    for i in range(97,123): # 97 => a 122 => z
        contar = Contarletra(chr(i),frase)
        print(f"{chr(i)} - {contar}")

frase = input("introduza a frase: ")
ContarFrequencia(frase)