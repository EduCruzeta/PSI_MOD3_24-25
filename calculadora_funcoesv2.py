#calculadora simples com funções 
def Somar(n1,n2):
    """ Função que recebe dois numeros e mostrar a sua subtração"""
    print(n1+n2)

def Subtrair(n1,n2):
    """ Função que recebe dois numeros e mostrar a sua subtração"""
    print(n1-n2)

def Multiplicar(n1,n2):
    """Função que recebe dois numeros e mostrar a sua multiplicação"""
    print(n1*n2)

def Dividir(n1,n2):
    """Função que recebe dois numeros e mostrar a divisão"""
    print(n1/n2)

def menu():
    """
    Mostrar ao utilizador as operacões que a calculadora vai realizar
    
    """
    op = 0
    while op != "5":

        print("1.Somar\n2.Subtrair\n3.Multiplicar\n4.Dividir\n5.Terminar")
        op = input("insira a operação que vai fazer: ")
        
        if op != "5":
            n1 = float(input("insira o primeiro valor: "))
            n2 = float(input("insira o segundo valor: "))
        if op =="1":
            Somar(n1,n2)
        elif op =="2":
           Subtrair(n1,n2)
        elif op == "3":
            Multiplicar(n1,n2)
        elif op == "4":
            Dividir(n1,n2)

def main():
    menu()

if __name__=="__main__":
    main()