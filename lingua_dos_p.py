"""Uma função que recebe uma palavra e devolve a mesma palavra convertida na lingua dos P
Alguns exemplos:
    Casa  -> Capasapa
    Bola  -> Bopolapa
    Olá   -> Opolápá
    Muito -> Muipuitopo
"""

def E_vogal(letra:str) -> str:
    """Função que devolve true ou false se a letra é vogal/consoante"""
    vogais="aeiouáàãéèêíìóòõúù"
    if letra.lower() in vogais:
        return True
    return False

def ConverteSilaba(silaba:str) -> str:
    """Função que recebe uma silaba e junta a mesma silaba na lingua dos P
    Ex: Ca -> Capa
        Mui -> Muipui
        O -> Opo
    """
    if E_vogal(silaba[0]):
        silaba = silaba + "p" + silaba.lowe()
    else:
        temp = "p"
        for i in range(1,len(silaba)):
            temp = temp + silaba[i]
        silaba = silaba + temp
    return silaba

def Converte(palavra:str)-> str:
    """Função que converte uma palavra na lingua dos P"""
    converte = ""
    for i in range(len(palavra)):
        if E_vogal(palavra[i]) and i > 0:
            #converter a silaba
            pass
        else:
            converte = converte + palavra[i]