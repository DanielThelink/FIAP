#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
#Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
#Calcule o preço a pagar de acordo com a tabela a seguir.

quantidade_kwh = float(input("Quantitade kwh:"))
tipo_de_instalacao = input("Digite o tipo de instalaçao (R,C,I):")

if tipo_de_instalacao == "R":
    if quantidade_kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo_de_instalacao == "C":
    if quantidade_kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo_de_instalacao == "I":
    if quantidade_kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60

else:
    preco = 0
    print("Erro!")

valor_a_pagar = quantidade_kwh * preco
print(valor_a_pagar)


