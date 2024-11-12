def Soma():
    """
    A função soma os valores 10 e 5
    """
    print(10+5)

def Soma2(x,y):
    """
    a função recebe dois valores e vai somar

    Exemplo:
    soma2(10,5)
    """
    print(x+y)


def main():
    Soma()
    Soma2(30,40)
    Soma2(-5,80)


#so vai executar o programa se ele for o principal 

if __name__=="__main__":
    main()