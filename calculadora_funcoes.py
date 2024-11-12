#este programa é uma calculadora com a nova materia das funções 

def soma(x,y):
    print(x+y)


def subtrair(x,y):
    print(x-y)


def div(x,y):
    print(x/y)


def multi(x,y):
    print(x*y)




def main():
    x = int(input("insira o primeiro valor: "))
    y = int(input("insira o segundo valor: "))
    operacao = input("insira a operaçao: ")
    
    if operacao == "s":
        soma(x,y)
    if operacao == "sub":
        subtrair(x,y)
    if operacao == "div":
        div(x,y)
    if operacao == "multi":
        multi(x,y)

if __name__=="__main__":
    main()