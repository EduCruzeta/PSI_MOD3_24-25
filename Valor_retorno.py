def Soma(x,y):
    t = x + y
    return t

def soma(x,y,):
    t = x + y 
    print(id(x))
    x = 0
    print(id(x))
    y = 0
    return t
x = Soma(10,5)
print(x)
print(soma(5,10))
print(Soma(5,10) + 5)
print(Soma(5,Soma(10,59)))
x = int(input("insira o valor 1: "))
y = int(input("insira o valor 2: "))
w = int(input("insira o valor 2: "))
print(Soma(x,y))