# Eduardo Cruz N5 10T

def Verificar_N_Perfeito():
    """Esta funçao vai ser responsável por verificar se o numero é perfeito ou não"""
    contar = 0
    numero = ler_numero_inteiro()
    for i in range(1,numero):
        if numero % i == 0:
            contar = contar + i

    if contar == numero:
        print("Número perfeito")
    else:
        print("Número não perfeito")

def ler_numero_inteiro(mensagem="Introduza um valor inteiro: ") -> int:
    """
    Função que lê do utilizador um nº inteiro. 
    A função garante que o valor inserido é um valor válido
    """
    while True:
        dados = input(mensagem)
        if len(dados)==0:
            continue
        # verificar se existe um - no inico da str (valor negativo)
        if dados[0] == "-":
            testar = dados.replace('-','')
        else: 
            testar = dados
        if dados.isdigit():
            return int(dados)
        print("Erro: o valor inserido não é valido")    

Verificar_N_Perfeito()