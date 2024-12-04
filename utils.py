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

def ler_numero_inteiro_entre(valor_min,valor_max = None, mesagem="introduza um valor inteiro: ")-> int :
    while True: 
        numero = ler_numero_inteiro()
        if numero >= valor_min and (valor_max is None or numero <= valor_max):
            return numero
        else:
            print("Erro: o valor inserido não é valido")

def ler_numero_decimal(mensagem="introduza um valor decimal: ") -> float:
    """
    Função para ler um nº decimal.
    A função garante que o valor é válido e aceita como separador das casas decimais . ou ,
    """
    
    while True: 
        dados = input(mensagem)
        if len(dados)==0:
            continue
        # substituir as virgulas por pontos

        dados = dados.replace(",",".")

        # verificar se existe um - no inico da str (valor negativo)
        if dados[0] == "-":
            testar = dados.replace('-','')
        else: 
            testar = dados

        # contar os pontos decimais

        pontos = testar.count('.')

        # remover pontos decimais

        testar = testar.replace(".","")

        # não pode ter mais de 1 ponto decimal e só pode ter digitos

        if testar.isdigit() and pontos <=1:
            return float(dados)
        
        print("Erro: o valor inserido não é valido")

def ler_numeros_decimais_entre(valor_min,valor_max = None,mensagem = "Introduza um valor decimal"):
    while True:
        numero = ler_numero_decimal()
        if numero >= valor_min and (valor_max is None or numero <= valor_max):
            return numero
        else:
            print("Erro: o valor inserido não é valido")