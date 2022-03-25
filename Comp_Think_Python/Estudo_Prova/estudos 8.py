#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
#assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km_percorridos = float (input("km percorridos:"))
quantidade_dias = int(input("quantidade dias:"))

#o calculo poderia ser feito de uma maneira mais curta assim:

#preco_total = 60 * quantidade_dias + 0.15 * km_percorridos

preco_dias = 60 * quantidade_dias

preco_km = 0.15 * km_percorridos

preco_a_pagar = preco_dias + preco_km

print(f"o valor total a pagar é de R${preco_a_pagar}")