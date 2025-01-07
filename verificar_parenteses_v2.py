"""
O programa vai ler a expressão inserida pelo utilizador e vai dizer se esta corretao 
ou nao com base nos parenteses curvos e retos
"""

#Pedir a expressão ao utilizador
expressao = input("Introduza uma expressão matemática:")
#Fazer a validação com uma função
def Validar(expressao):
    """
    Função que recebe uma expressão matemática para validade os ()
    A função devolve falso se a expressão tiver erros de outra forma devolve true
    """
    abriu = ""
    for l in expressao:
        if l == '(' or l == '[':
            abriu = abriu + l
        if l == ')' or l== ']':
            if abriu == "":
                return False
            ultimo = abriu[len(abriu)-1]
            if (ultimo == ' (' and l == ')') or (ultimo == '[' and l == ']'):
                temp = abriu
                # limpar a string para copiar todos os caracteres menos o último
                abriu = ""
                for i in range(len(temp)-1):
                    abriu = abriu + temp[i]
            else:
                return False
    if abriu == "":
        return True
    return False

#chamar a função
resultado = Validar(expressao)

#indicar se a expressão é ou não valida
if resultado == False:
    print("A expressão não é válida.")
else:
    print("A expressão é valida.")