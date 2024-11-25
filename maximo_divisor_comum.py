#Esta função vai indicar o maximo divisor comum entre dois numeros

def Maximo_divisor(v1,v2):
    if v1 < v2:
        menor = v1
    else:
        menor = v2

    resultado = None
    for i in range(2,menor):
        if v1 % i == 0 and v2 % i == 0:
            resultado = i

    return resultado
            

def main():
    v1 = int(input("insira o primeiro valor: "))
    v2 = int(input("insira o segundo valor: "))
    Maximo_divisor(v1,v2)
    print(Maximo_divisor(v1,v2))

if __name__=="__main__":
    main()
