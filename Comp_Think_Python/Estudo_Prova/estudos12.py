#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, de 15%.

salario_funcionario = float(input("salario:"))

if salario_funcionario > 1250:

    aumento_menor = 10/100 * salario_funcionario + salario_funcionario

    print(f"seu salario teve um aumento de 10%, seu novo valor a receber é de R${aumento_menor}")

else:
    aumento_maior = 15/100 * salario_funcionario + salario_funcionario

    print(f'seu salario teve um aumento de 15%, seu novo salario é de R${aumento_maior}')