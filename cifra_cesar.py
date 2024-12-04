"""
O programa que codifica ou descodifica uma mensagem com base nos alfabetos fornecidos
"""
original = "abcdefghijklmnopqrstuvwxyz"
codigo = "bcdefghijklmnopqrstuvwxyza"

def menu():
    """
    Função para ler a opção do utilizador e executar a função adequada: codificar ou descodificar
    """
    print("""codificar:1
descodificar:2 """)
    escolha = int(input("insira a sua escolha: "))
    if escolha == 1:
        mensagem = input("insira o texto que quer codificar: ")
        mensagem = mensagem.lower()
        codificar(mensagem)
        print(codificar(mensagem))
    elif escolha == 2:
        mensagem_codificada = input("insira o texto codificado: ")
        mensagem_codificada = mensagem_codificada.lower()
        descodificar(mensagem_codificada)
        print(descodificar(mensagem_codificada))
def codificar(mensagem:str)->str:
    """
    Função que recebe uma mensagem e devolve a mesma
    codificada de acordo com o alfabetos fornecidos
    """
    global original
    global codigo
    texto = ""
    for l in mensagem:
        if l not in original:
            texto = texto + l
        for P in range(len(original)):
            if l==original[P]:
                texto = texto + codigo[P]
       
    return texto


def descodificar(mensagem_codificada:str)->str:
    """
    Função que recebe uma mensagem codificada e devolve a mesma 
    descodificada de acordo com os alfabetos fornecidos
    """
    global original
    global codigo
    texto = ""
    for l in mensagem_codificada:
        if l not in codigo:
            texto = texto + l
        for P in range(len(codigo)):
            if l==codigo[P]:
                texto = texto + original[P]

    return texto

def main():
    menu()

if __name__ == '__main__':
    main()