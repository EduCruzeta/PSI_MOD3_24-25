"""Completa as seguintes funções"""

def E_Impar(numero:int) -> bool:
    """Devolve true se o numero é impar e false se par"""
    if numero % 2 == 0:
        return False
    else:
        return True

print("Testes E_Impar")
assert E_Impar(10) == False, "Erro no primeiro teste. Devia dar False"
assert E_Impar(11) == True, "Erro no segundo teste. Devia dar True"
print("Completou testes E_Impar")

############################################################################
def Ola_User(nome:str):
    """Diz olá ao user. Se nome não estiver preenchido não diz nada"""
    if len(nome) < 0:
        return ("")
    else:
        return (f"Olá" ,{nome})

print("Testes Ola_User")
Ola_User("")        #Com este argumento não deve mostrar nada
Ola_User("Joaquim") #Com este argumento deve mostrar Olá Joaquim
print("Completou testes Ola_User")

#############################################################################
def JuntaDoisNomes(nome1:str,nome2:str) -> str:
    """Devolve os nomes numa string separados por um espaço em branco. O primeiro nome deve ser o que alfabeticamente for menor."""
    if nome1 < nome2:
        return f"{nome1} {nome2}"
        #return nome1 + " " + nome2
    
    return f"{nome2} {nome1}"

print("Testes JuntaDoisNomes")
assert JuntaDoisNomes("Joaquim","Ana") == "Ana Joaquim", "Erro no quinto teste, devia dar Ana Joaquim"
assert JuntaDoisNomes("Maria","Zé") == "Maria Zé","Erro no sexto teste, devia dar Maria Zé"
print("Completou testes JuntaDoisNomes")

#############################################################################
maior = ""

def QualOMaior(nome1:str, nome2: str):
    """Função para alterar a variável global maior guardando o nome com mais letras. Caso sejam de igual tamanho deve guardar a palavra Iguais"""
    global maior
    if len(nome1) > len(nome2):
        maior = nome1
    elif len(nome1) < len(nome2):
        maior = nome2
    else:
        maior = "Iguais"


print("Testes QualOMaior")
QualOMaior("Ana","Maria")
assert maior == "Maria", "Erro no sétimo teste, maior devia ser Maria"
QualOMaior("João","José")
assert maior == "Iguais", "Erro no oitavo teste, maior devia ser Iguais"
QualOMaior("António","Zé")
assert maior == "António", "Erro no nono teste, maior devia ser António"
print("Completou testes QualOMaior")

##################################################################################
cartas = "23456QJK7A"

def CartaMaisForte(carta1:str, carta2:str) -> str:
    """Função que recebe duas cartas de um baralho e devolve a mais forte ou None caso sejam iguais"""
    global cartas
    if carta1 == carta2:
        return None
    p1 = 0
    for c in cartas:
        if c == carta1:
            break
        p1 = p1 + 1

    p2 = 0
    for c in cartas:
        if c == carta2:
            break
        p2 = p2 + 1

    if p1 > p2:
        return carta1
    
    return carta2
    


print("Testes CartaMaisForte")
assert CartaMaisForte("2","3") == "3", "Erro no décimo teste, devia devolver 3"
assert CartaMaisForte("A","A") == None, "Erro no décimo primeiro teste, devia devolver None"
assert CartaMaisForte("K","7") == "7", "Erro no décimo segundo teste, devia devolver 7"
print("Completou testes CartaMaisForte")