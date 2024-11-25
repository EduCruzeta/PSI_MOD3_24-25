# programa para ler as notas de 3 alunos e calcular a média
from mediafuncoes import FuncaoD 

nota1 = int(input("introduza uma nota: "))
nota2 = int(input("introduza uma nota: "))
nota3 = int(input("introduza uma nota: "))

media = FuncaoD(nota1,nota2,nota3)

print("A média das notas é de",media)