
def somar(x,y):
    print(x+y)
    x = 0
    y = 0

def main():
    somar("joaquim","maria")
    somar(10,5)
    somar(10.3,3.1)
    n = 10
    z = 15
    somar(n,z)
    print(n,z)

if __name__== "__main__":
    main()