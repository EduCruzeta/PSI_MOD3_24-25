# programa para ler as notas de 3 alunos e calcular a média
import mediafuncoes # ou import funcaoD from mediafuncoes

nota1 = int(input("introduza uma nota: "))
nota2 = int(input("introduza uma nota: "))
nota3 = int(input("introduza uma nota: "))

media = mediafuncoes.FuncaoD(nota1,nota2,nota3)

print("A média das notas é de",media)