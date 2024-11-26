#este algoritmo vai simular de parque de estacionamento e a cada 15 min vai pagar um valor
from datetime import datetime


def DuracaoEstacionamento(hora:int,minutos:int) -> int: 
    """
    Função que calcula a duração do estacionamento em minutos 
    com base nos valores dos parametros e a hora atual
    """
    hora_atual = datetime.now().hour
    minutos_atuais = datetime.now().minute
    n_horas = hora_atual - hora
    n_minutos = minutos_atuais - minutos
    if n_minutos < 0:
        n_horas -= 1
        n_minutos = 60 - minutos + minutos_atuais
    duracao_total_minutos = n_horas * 60 + n_minutos

    return duracao_total_minutos

def blocos_min(minutos:int)-> int:
    """
    Função que recebe a duração em minutos e 
    devolve quantos locos de 15 min existem
    """
    
    n_blocos = minutos // 15
    if minutos % 15 != 0:
        n_blocos += 1
    
    return n_blocos

def Custo(blocos:int,preco_bloco:float) -> float:  
    """
    Função que calcula o custo do estacionamento com base 
    na duração em minutos e o preço por cada bloco de 15 minutos
    """ 
    return blocos * preco_bloco


def main():
    #ler dados
    hora = int(input("insira a hora que entrou: "))
    minutos = int(input("insira os minutos em que entrou: "))
    preco_bloco = float(input("insira o preço de cada bloco de 15 min: "))
    #calcular a duração em minutos
    duracao_minutos=DuracaoEstacionamento(hora,minutos)
    blocos = blocos_min(duracao_minutos)
    #calcular o custo
    custo = Custo(blocos,preco_bloco)
    #mostrar o resultado
    print(f"O estacionamento com duração de {duracao_minutos} minutos que corresponde a {blocos} blocos de 15 min teve o custo de {custo}€")

if __name__=="__main__":
    main()




