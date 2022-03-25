#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
#O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
#O valor da prestação mensal não pode ser superior a 30% do salário.
#Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("digite o valor em R$ da casa:"))
salario = float(input("Digite o valor de seu salario:"))
quantidade_anos_pagar = int(input("Digite a quantidade de anos que voce pretende pagar:"))
#aqui eu converto a quantidade de anos para meses
conversao_meses = quantidade_anos_pagar * 12
#aqui eu pego o valor de 30% do valor total do salario
porcent_salario = salario * 30/100
# aqui eu calculo o valor da prestaçao em meses
valor_prestacao = valor_casa / conversao_meses
# condicao para o emprestimo ser aprovado
if valor_prestacao <= porcent_salario:
   print(f"Seu empréstimo foi aprovado! o valor dar prestacoes ficaria R${valor_prestacao}")

else:
    print("Infelizmente nao podemos aprovar o seu emprestimo.") #batata