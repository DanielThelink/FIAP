#Refaça o exercício 4, identificando o conceito aprovado (média superior ou igual a 6),
#exame (média maior ou igual a 4 e menor que 6) ou reprovado (média inferior a 4).

Nota1 = float(input("Nota1:"))
Nota2 = float(input("Nota2:"))

media = (Nota1 + Nota2) / 2
print(media)

if media >= 6:
    print("Aprovado!")

elif media >=4 and media < 6:
    print("Exame")

else:
    print("Reprovado")
