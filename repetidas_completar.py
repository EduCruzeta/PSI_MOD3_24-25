#Completa a função de acordo com a docstring
def Repetidas(palavra):
    """
    Recebe uma string com um texto que deve ser verificado para encontrar letras repetidas
    Parâmetro:
        texto: string a verificar
    Devolve:
        True: se o texto contém letras repetidas
        False: se o texto só tem letras únicas (sem repetições)
    """     

    palavra = palavra.lower()

    for letra in palavra:
        
        


#Testes
assert Repetidas("banana") == True, "Erro a função devia devolver True"
assert Repetidas("Ana") == True, "Erro a função devia devolver True"
assert Repetidas("José") == False, "Erro a função devia devolver False"
assert Repetidas("") == False,"Erro a função devia devolver False"
assert Repetidas("Tubarão") == False, "Erro a função devia devolver False"

print("Função passou nos testes")