salario_funcionario = float(input("salario:"))

if salario_funcionario <= 400:

    aumento = 15/100 * salario_funcionario + salario_funcionario
    percentual = 15
    reajuste = salario_funcionario * 15 / 100
    print("Reajuste Ganho:", reajuste)
    print("Em percentual:", percentual,"%")
elif salario_funcionario > 400.01 and salario_funcionario <= 800:
    aumento = 12 / 100 * salario_funcionario + salario_funcionario
    percentual = 12
    reajuste = salario_funcionario * 12 / 100
    print("Reajuste Ganho:", reajuste)
    print("Em percentual:", percentual,"%")
elif salario_funcionario > 800.01 and salario_funcionario <= 1200:
    aumento = 10 / 100 * salario_funcionario + salario_funcionario
    percentual = 10
    reajuste = salario_funcionario * 10 / 100
    print("Reajuste Ganho:", reajuste)
    print("Em percentual:", percentual,"%")

elif salario_funcionario > 1200.01 and salario_funcionario <= 2000:
    aumento = 7 / 100 * salario_funcionario + salario_funcionario
    percentual = 7
    reajuste = salario_funcionario * 7 / 100
    print("Reajuste Ganho:", reajuste)
    print("Em percentual:", percentual,"%")

elif salario_funcionario > 2000:
    aumento = 4 / 100 * salario_funcionario + salario_funcionario
    percentual = 4
    reajuste = salario_funcionario * 4/100
    print("Reajuste Ganho:", reajuste)
    print("Em percentual:", percentual,"%")

print(f"Novo Salario: {aumento:.2f}")