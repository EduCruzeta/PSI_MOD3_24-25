

#for i in range(10):
    #print(i)
    #i = 0

def FuncaoA():
    x = 0
    while x < 10:
        x = x + 1
        return x
    
print(FuncaoA())



def FuncaoB():
    x = 0
    while x < 10:
        x = x + 1
        yield x # devolve o valor e mantém o estado

for i in FuncaoB():
    print(i)
    i = 0
    