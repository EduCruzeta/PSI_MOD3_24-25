"""este algoritmo vai ter uma função que faz os quadrados dos numeros e depois 
uma que vai calcular a soma dos inteiros desses quadrados ate ao n escolhido"""
from N_quadrado import N_quadrado

def Soma_quadrados(valor1):
    contar = 0
    for i in range(1,valor1+1):
        resultado = N_quadrado(i)
        contar = contar + resultado
    
    return contar





valor1 = int(input("insira o valor: "))
print(Soma_quadrados(valor1))