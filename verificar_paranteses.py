"""
O programa vai ler a expressão inserida pelo utilizador e vai dizer se esta corretao ou nao com base nos parenteses
"""

#Pedir a expressão ao utilizador
expressao = input("Isntroduza uma expressão matemática:")
#Fazer a validação com uma função
def Validar(expressao):
    """
    Função que recebe uma expressão matemática para validade os ()
    A função devolve falso se a expressão tiver erros de outra forma devolve true
    """
    contar = 0
    for l in expressao:
        if l == '(':
            contar = contar + 1
        if l == ')':
            contar = contar - 1
        if contar < 0:
            return False
    if contar == 0:
        return True
    return False

#chamar a função
resultado = Validar(expressao)

#indicar se a expressão é ou não valida
if resultado == False:
    print("A expressão não é válida.")
else:
    print("A expressão é valida.")