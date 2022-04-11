##### 1
'''
velocidade = float(input("Velocidade em KM/h ="))

if velocidade > 80:
    print("Voce foi multado em R$ 5 por estar acima de 80hm/h")
'''

##### 2
'''
num_1 = int(input("numero a ="))
num_2 = int(input("numero b ="))
num_3 = int(input("numero c ="))
'''

##### 3

'''
valor_salario = float(input("valor salario ="))

if valor_salario > 1250:
    # aqui ele calcula 10% de reajuste no valor do salario colocado na variavel
    reajuste_1 =(10/100) * valor_salario

    # aqui ele soma o valor do reajuste com o valor do salario
    valor_superior = reajuste_1 + valor_salario

    print("seu novo salario com o reajuste de 10% =",valor_superior)
else: # se o salario foi inferior a "R$1250" ele ira executar o codigo abaixo

    # aqui ele calcula 10% de reajuste no valor do salario colocado na variavel
    reajuste_2 =(15/100) * valor_salario
    # aqui ele soma o valor do reajuste com o valor do salario
    valor_inferior= reajuste_2 + valor_salario
    print("seu novo salario com o reajuste de 15% =",valor_inferior)
'''
