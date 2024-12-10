"""
este programa vai ler o saque que os ladroes fizera me vai dividir o 
lider fica com metade outros dois ficam com o mesmo e o condutor fica 
com metade dos outros 2 ou seja 50/20/20/10
"""
import math
def Pedir_saque():
    saque = 0
    while saque < 0:
        saque = float(input("insira o tamanho do saque realizado: "))
    return saque

def Dividir_lucros(saque):
    global lider
    global capangas
    global condutor
    lider = round(saque * 0.50,2)
    print(f"O Lider recebe {lider}€")
    capangas = round(saque * 0.20,2)
    print(f"Os capangas recebem {capangas}€ cada um.")
    condutor = round(saque * 0.10,2)
    print(f"O condutor recebe{condutor}€")

def Calcular_meses(valor):
    """
    Monstra em quantos meses se vai gastar o dinheiro.
    """
    # calcular 5%
    valor_mes = valor * 0.05
    # verificar se ultrapassa 1000€
    if valor_mes > 1000:
        valor_mes = 1000
    # calcular quantos meses demora a gastar o dinheiro todo
    meses = valor / valor_mes
    meses = math.ceil(meses)
    print(f"Os {valor}€ são gastos em {meses} meses, gastando {valor_mes}€ por mes.")
      

def main():
    saque = Pedir_saque()
    Dividir_lucros(saque)
    Calcular_meses(lider)
    Calcular_meses(capangas)
    Calcular_meses(condutor)


  
if __name__=="__main__":
    main()    