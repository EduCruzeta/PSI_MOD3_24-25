#este algoritmo vai ter uma função que recebe a medida dos catetos e calcula a hipotenusa
import math

def Hipotenusa(cateto1,cateto2):
    hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
    return hipotenusa



def main():
    cateto1 = int(input("insira o valor do cateto 1: "))
    cateto2 = int(input("insira o valor do cateto 2: "))
    Hipotenusa(cateto1,cateto2)
    hipotenusa = round(Hipotenusa(cateto1,cateto2),3)
    print(hipotenusa)

if __name__=="__main__":
    main()