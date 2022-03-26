renda = float(input("renda:"))

if renda <= 2000.00:
    print("isento")
elif renda > 2000.01 and renda <= 3000.00:
    reajuste = 0.08 * (renda - 2000)

elif renda > 3000.01 and renda <= 4500.00:
    reajuste = (renda - 3000) * 0.18 + (1000 * 0.08)

elif renda > 4500.00:
    reajuste = (renda - 4500) * 0.28 + (1000 * 0.08) + (1500 * 0.18)

print(f"R$ {reajuste:.2f}")



