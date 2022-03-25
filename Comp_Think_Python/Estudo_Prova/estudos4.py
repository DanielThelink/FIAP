#Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salário.

salario = float(input("salario:"))
porcentagem_aumento = int(input("aumento:"))

valor_aumento = porcentagem_aumento/100 * salario

novo_salario = valor_aumento + salario

print(f"o valor do aumento de acordo com a porcentagem dada foi de R${valor_aumento},"
      f"o valor total do salario foi de R${novo_salario}")