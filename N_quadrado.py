#este algoritmo vai ter uma função que tem uma função que recebe um valor e da o valor dele ao quadrado
import math

def N_quadrado(valor):
    valor = valor ** 2
    return valor

def main():
    valor1 = int(input("insira o valor: "))
    N_quadrado(valor1)
    print(N_quadrado(valor1))

if __name__=="__main__":
    main()