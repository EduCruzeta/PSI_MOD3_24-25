#este programa vai ler as cordenadas do utilizador e informar em que quadrante se encontra
import utils


def Quadrantes(x,y):
    if x == 0 and y == 0:
        return "Esta no centro."
    elif x > 0 and y > 0:
        return "Está no 1º Quadrante."
    elif x < 0 and y < 0:
        return "Está no 3º Quadrante."
    elif x < 0 and y > 0:
        return "Está no 2º Quadrante."
    elif x > 0 and y < 0:
        return "Está no 4º Quadrante."    
    else:
        return "Não está em nenhum quadrante"

def main():
    x = float(input("Insira a cordenada do ponto X: "))
    y = float(input("Insira a cordenada do ponto Y: "))
    print(Quadrantes(x,y))


if __name__=="__main__":
    main()