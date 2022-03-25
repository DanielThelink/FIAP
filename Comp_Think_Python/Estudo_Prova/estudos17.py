#Faça um programa que leia 2 notas de um aluno,
#calcule a média e imprima aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6).

Nota1 = float(input("Nota1:"))
Nota2 = float(input("Nota2:"))

media = (Nota1 + Nota2) / 2
print(media)

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado...")