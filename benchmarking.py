import math
from datetime import datetime

#calcula a exponenciação utilizando o operador **
def funcao_complicada():
    for i in range(100000):
        _ = i ** 2

#calcula a exponenciação utilizando a função pow do módulo math
def funcao_complicada2():
    for i in range(1000000):
        _ = math.pow(i,2)

def medir_tempo():
    inicio = datetime.now()
    funcao_complicada()
    fim = datetime.now()
    tempo_execucao = fim - inicio
    print("Tempo de execução:",tempo_execucao.total_seconds())

medir_tempo()