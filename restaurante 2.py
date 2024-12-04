
"""
O Sr Joaquim precisa de um programa para controlar o nº de clientes e de mesas do seu restaurante.
O programa deve apresentar um menu com as opções:
1. Entrada
2. Saída
3. Estado
4. Terminar
Quando o programa arranca deve ler do utilizador o nº de mesas e o nº de clientes que o restaurante pode receber
De  cada vez que entram clientes devem perguntar quantos clientes estão a entrar e quantas mesas vão ocupar
De cada vez que saíem clientes devem perguntar quantos clientes saíram, quantas mesas libertaram e qual o custo da refeição
A opção estado deve indicar quantas mesas estão livres e ocupadas, quantos clientes estão no restaurante e a percentagem de ocupação (de clientes) e o custo de todas as refeições do clientes que já sairam do restaurante
O programa só deve terminar quando é escolhida a opção 4
O programa não deve permitir entradas de dados que não sejam válidas.
"""

import utils

def Entrada_Clientes(clientes_max,n_atual_clientes):
    """Pergunta quantos clientes estão a entrar e quantas mesas vão ocupar"""
    #testar se o restaurante não pode receber mais clientes
    if n_atual_clientes == clientes_max:
        print("Restaurante está cheio")
        return 0
    # ler o nº de clientes a entrar
    lugar_livres=clientes_max - n_atual_clientes
    clientes_entrada=utils.ler_numero_inteiro_limites(1,lugar_livres,"Indique o número de clientes que estão a entrar: ")
    #devolve o nº de clientes que entraram
    return clientes_entrada
    

    
def Entrada_Mesas(mesas_max,n_atual_mesas):
    """Pergunta quantos quantas mesas vão ocupar"""
    if n_atual_mesas == mesas_max:
        print("Restaurante está cheio")
        return 0
    # ler o nº de mesas a entrar
    mesas_livres=mesas_max - n_atual_mesas
    mesas_entrada=utils.ler_numero_inteiro_limites(1,mesas_livres,"Indique o número de mesas que vão ocupar: ")
    #devolve o nº de mesas que entraram
    return mesas_entrada
    
    
def Saída_Clientes(n_atual_clientes):
    """Pergunta quantos clientes saíram"""
    if n_atual_clientes==0:
        print("Não tem clientes")
        return 0
    n_clientes=utils.ler_numero_inteiro_limites(1,n_atual_clientes,"Quantos clientes saiem do restaurante: ")
    return n_clientes


def Saída_Mesas(n_atual_mesas):
    """Pergunta quantas mesas libertaram"""
    if n_atual_mesas==0:
        print("Não tem mesas ocupadas.")
        return 0
    n_mesas=utils.ler_numero_inteiro_limites(1,n_atual_mesas,"Quantas  ficaram desocupadas: ")
    return n_mesas

    
def Estado(mesas_max,clientes_max,n_atual_clientes,n_atual_mesas,tcusto_refeição):
    """Indica quantas mesas estão livres e ocupadas, quantos clientes estão no restaurante e a percentagem
    de ocupação (de clientes) e o custo de todas as refeições do clientes que já sairam do restaurante"""
    print(f"Tem {mesas_max} mesas ocupadas e {mesas_max-n_atual_mesas} mesas livres")
    print(f"Tem {clientes_max} clientes no restaurante")
    print(f"Que corresponde a uma ocupação de {n_atual_clientes/clientes_max*100}%")
    print(f"Já recebeu {tcusto_refeição}€ das refeições servidas")
    

def Menu():
    mesas_max=utils.ler_numero_inteiro("Introduza o número de mesas: ")
    clientes_max=utils.ler_numero_inteiro("Introduza o número de clientes: ")
    op=1
    n_atual_mesas = 0
    n_atual_clientes = 0
    tcusto_refeição=0 #acumular o valor pago pelas refeições dos clientes
    while op !=4:
        op=utils.ler_numero_inteiro_limites(1,4,"1.Entrada\n2.Saída\n3.Estado\n4.Terminar")
        if op == 1:
            #Entrada dos clientes
            n_clientes_entraram=Entrada_Clientes(clientes_max,n_atual_clientes)
            n_mesas_ocupadas   =Entrada_Mesas(mesas_max,n_atual_mesas)
            n_atual_clientes   =n_atual_clientes + n_clientes_entraram
            n_atual_mesas      =n_atual_mesas+n_mesas_ocupadas 


        if op ==2:
            #Saída dos clientes
            n_clientes_saída=Saída_Clientes(n_atual_clientes)
            n_mesas_desocupadas=Saída_Mesas(n_atual_mesas)
            n_atual_clientes= n_atual_clientes - n_clientes_saída
            n_atual_mesas=n_atual_mesas-n_mesas_desocupadas
            #evitar custo da refeição quando n saiu nenhum cliente do restaurante
            if n_clientes_saída>0 or n_mesas_desocupadas>0:
                pagou=utils.ler_numero_decimal_limites(0,None,"Quanto custou a refeição: ")
                tcusto_refeição += pagou



        if op ==3:
            Estado(mesas_max,clientes_max,n_atual_clientes,n_atual_mesas,tcusto_refeição)


        if op ==4:
            break   


def main():
    Menu()
if __name__=="__main__":
    main()
