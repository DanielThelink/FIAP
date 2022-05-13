###### 1

'''
a = 5
b = 5
print (a + b)
'''

###### 2
'''
metros = float(input("Metros ="))

resultado = metros * 1000
print("o valor em milimetros é", resultado)
'''
###### 3
'''
dias = int(input("Dias :"))
horas = float(input("horas :"))
minutos = int(input("minutos :"))
segundos = float(input("segundos:"))

total_seg = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print(total_seg)
'''
###### 4
'''
salario_inicial = float(input("Salario ="))
porcentagem_aumento = float(input("Aumento ="))

# pega o valor do salario e divide pelo aumento salarial

valor_aumento = salario_inicial * (porcentagem_aumento/100)

# aqui ele ira calcular a porcentagem pegando o valor "calc" e multiplicar por 100

valor_novo_salario = salario_inicial + valor_aumento

print("o valor do aumento é R$ %.2f"%valor_aumento)
print("o valor do seu novo salario é R$ %.2f"%valor_novo_salario)
'''

###### 5
'''
valor_mercadoria = float(input("valor mercadoria ="))
valor_porcentagem = float(input("valor desconto = "))

valor_desconto = valor_mercadoria * valor_porcentagem / 100

print("o valor do desconto de {}% de R${} é de R$ =".format(valor_porcentagem,valor_mercadoria), valor_desconto)

# aqui ele pega o valor da mercadoria e subtrai o valor do desconto para conseguir o valor total a pagar

valor_a_pagar = valor_mercadoria - valor_desconto
print("o valor total a pagar é de = R$", valor_a_pagar)
'''
###### 6
'''
distancia_percorrida = float(input("Distancia percorrida ="))
velocidade_media = float(input("Velocidade media ="))

tempo_de_viagem = distancia_percorrida / velocidade_media

print(tempo_de_viagem)
'''
###### 7
'''
valor_celcius = float(input("valor em celcius = "))


valor_f = valor_celcius * 1.8 + 32

print("O valor de {}ºC equivale a {}°F ".format(valor_celcius , valor_f))
'''

###### 8
'''
km_percorridos = float(input("KM percorridos = "))
quantidade_dias = int(input("quantidade de dias = "))

# o carro alugado custa 60 reais por dia, e 0.15 centavos por KM percorrido.

total_pagar = (60 * quantidade_dias) + (0.15 * km_percorridos)

print("voce tera que pagar R$ {}" .format(total_pagar))
'''
###### 9
'''
x = int(input("x="))
y = int(input("y="))

#**2 seria elevado ao quadrado

z= (x*x + y*y) / (x-y)**2

print (z)
'''
###### 10

salario = float(input("salario ="))

reajuste = (35/100) * salario
novo_salario = salario + reajuste
print ("novo salario =",novo_salario)
