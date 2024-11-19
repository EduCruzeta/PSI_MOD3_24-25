# a) a função deve ler do utilizador os 3 numeros, calcular e mostrar a média.
# b) a função deve receber os 3 numeros, calcular e mostrar a média
# c) a função deve ler do utilizador os 3 numeros, calcular e devolver a média
# d) a função deve receber os 3 numeros, calcular e devolver a média


def FuncaoA():
    v1 = int(input("insira o primeiro valor: "))
    v2 = int(input("insira o segundo valor: "))
    v3 = int(input("insira o terceiro valor: "))
    media = (v1 + v2 + v3) / 3
    print(media)

def FuncaoB(v1,v2,v3):
    media = (v1 + v2 + v3) / 3
    print(media)

def FuncaoC():
    v1 = int(input("insira o primeiro valor: "))
    v2 = int(input("insira o segundo valor: "))
    v3 = int(input("insira o terceiro valor: "))
    media = (v1 + v2 + v3) / 3
    return(media)

def FuncaoD(v1,v2,v3):
    media = (v1 + v2 + v3) / 3
    return(media)

def main():
    v1 = int(input("insira o primeiro valor: "))
    v2 = int(input("insira o segundo valor: "))
    v3 = int(input("insira o terceiro valor: "))
    #FuncaoA()
    #FuncaoB(v1,v2,v3)
    #print(FuncaoC())
    print(FuncaoD(v1,v2,v3))




if __name__== "__main__":
    main()