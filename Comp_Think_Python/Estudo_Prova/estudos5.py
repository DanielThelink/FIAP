#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar.

preco_mercadoria = float(input("preco mercadoria:"))
percentual_desconto = int(input("desconto:"))

valor_desconto = (percentual_desconto/100) * preco_mercadoria

preco_a_pagar = preco_mercadoria - valor_desconto

print(f"o valor do desconto é de R${valor_desconto}, e o preço a pagar é de R${preco_a_pagar}")