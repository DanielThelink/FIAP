#Escreva um programa que pergunte a velocidade do carro de um usuário.
#Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h.

velocidade_carro = float(input("velocidade:"))

if velocidade_carro > 80:

    multa = (velocidade_carro - 80) * 5

    print(f"voce ultrapassou a velocidade de 80km/h, portanto terá que pagar uma multa no valor de R${multa} ")

else:
    print("Salvo pelo gongo")