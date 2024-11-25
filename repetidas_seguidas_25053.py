#Completa a função de acordo com a docstring
def RepetidasSeguidas(palavra) -> str:
    """
    Recebe uma string com um texto que deve ser verificado para encontrar letras seguidas iguais
    Parâmetro:
        texto: string a verificar
    Devolve:
        True: se o texto contém letras seguidas iguais
        False: se o texto não tem letras seguidas iguais
    """

    letra_anterior = ""
    palavra = palavra.lower()
    for letra in palavra:
        if letra == letra_anterior:
            return True
        else:
            letra_anterior = letra
    
    return False

#Testes
assert RepetidasSeguidas("Ana") == False, "Erro a função devia devolver False"
assert RepetidasSeguidas("Assar") == True, "Erro a função devia devolver True"
assert RepetidasSeguidas("") == False,"Erro a função devia devolver False"
assert RepetidasSeguidas("AsSado") == True, "Erro a função devia devolver False"

print("Função passou nos testes")