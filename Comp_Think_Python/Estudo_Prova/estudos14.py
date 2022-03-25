#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
#Você deve poder calcular soma, subtração, multiplicação e divisão.
#Exiba o resultado da operação solicitada.

num_1 = int(input("numero 1:"))
num_2 = int(input("numero 2:"))
operacao = input("Digite a operacao desejada (+,-,*,/):" )
if operacao == "+":

    resultado = num_1 + num_2

elif operacao == "-":

    resultado = num_1 - num_2

elif operacao == "*":

    resultado = num_1 * num_2

elif operacao == "/":

    resultado = num_1 / num_2


else:
    print("operaçao invalida!")

print(f"o resultado da operacao:{operacao} é de {resultado}")

