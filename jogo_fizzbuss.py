# Exercicio FizzBuzz
def Fizzbuzz(upTo):
    for i in range(1,upTo+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz",end=" ")
        elif i % 3 == 0:
            print("Fizz",end=" ")
        elif i % 5 == 0:
            print("Buzz",end=" ")
        else:
            print(i,end=" ")
    
Fizzbuzz(35)

print("--------------------------------------------------------")

# Exercicio FizzBuzz v2
def Fizzbuzz_v2(upTo):
    for i in range(1,upTo+1):
        if i % 15 == 0:
            print("FizzBuzz",end=" ")
        elif i % 3 == 0:
            print("Fizz",end=" ")
        elif i % 5 == 0:
            print("Buzz",end=" ")
        else:
            print(i,end=" ")
    
Fizzbuzz_v2(35)

print("--------------------------------------------------------")

# Exercicio FizzBuzz v3
def Fizzbuzz_v3(upTo):
    for i in range(1,upTo+1):
        print("fizzbuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i),end=" ")
    
Fizzbuzz_v3(35)

