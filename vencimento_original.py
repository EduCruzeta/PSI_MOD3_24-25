"""
Programa para calcular o vencimento de um trabalhador.
O programa deve começar por solicitar ao trabalhador que indique o seu nome,
 quantas horas trabalhou por dia, e quanto ganha por hora. Caso o trabalho tenho mais 
 do que 8 horas de trabalho deve receber, por cada hora extra recebe mais 25%. 
 Caso tenho trabalho mais do que 10 horas por dia deve receber 50% por cada hora além das 10 horas.
"""
import datetime

def PedirNomeTrabalhador():
    """Esta função deve pedir o nome do trabalhador. O nome deve ter pelo menos 3 letras."""
    nome = ""
    while len(nome)<3:
        nome = input("insira o seu nome: ")   
    return nome    
def PedirHorasTrabalho():
    """Esta função pede ao utilizador quantas horas trabalho no dia. O nº de horas deve ser superior a zero."""
    horas = 0
    while horas <= 0: 
        horas = int(input("insira o numero de horas que trabalhou: "))
    return horas

def PedirOrdenado():
    """Esta função pede ao utilizado quanto ganha por cada hora de trabalho"""
    ordenado_por_hora = 0
    while ordenado_por_hora <= 0:
        ordenado_por_hora = float(input("Insira quanto ganha por hora: "))
    return ordenado_por_hora

def MostrarVencimento(nome,horas,ordenado_por_hora):
    """Esta função deve mostrar o nome do trabalhador e quanto é que deve receber pelo dia de trabalho"""
    if horas >= 8:
        horas_normais = 8
    else:
        horas_normais = horas
    horas_extra = horas - 8
    # horas com o bonus de 25%
    if horas_extra > 2:
        horas_extra = 2
    # horas com bonus de 50%
    horas_extra_extra = horas - horas_normais - horas_extra
    if horas_extra < 0:
        horas_extra = 0
    if horas_extra_extra < 0:
        horas_extra_extra = 0
    ordenado = (horas_normais * ordenado_por_hora) + (horas_extra * ordenado_por_hora * 1.25) + (horas_extra_extra * ordenado_por_hora * 1.5)

    print(f"{nome} vai receber {ordenado}€ por {horas} horas de trabalho")


def main():
    # pedir o nome do trabalhador
    nome = PedirNomeTrabalhador()
    # pedir as horas que trabalhou
    horas = PedirHorasTrabalho()
    # pedir o ordenado por hora
    ordenado = PedirOrdenado()
    # calcular e mostrar o vencimento
    MostrarVencimento(nome,horas,ordenado)

if __name__=="__main__":
    main()