tickets = []
validacao = []
soma = 0
media = None
contador_elementos = 0
confirmacao = (input(
                    "1 - Adicionar Valores de Vendas\n"
                    "2 - Medias dos valores digitados\n"
                    "3 - Comparção dos valores com a media obtida\n"
                    "Digite o numero do serviço:"))
while confirmacao != "0":
    if confirmacao == "1":
        while confirmacao == "1":

            addticket = float(input("Adicione os valores das vendas aqui:"))
            tickets.append(addticket)
            contador_elementos += 1
            if addticket == 0:
                tickets.pop()
                contador_elementos = contador_elementos - 1
                confirmacao = input("1 - Adicionar Valores de Vendas\n"
                                    "2 - Medias dos valores digitados\n"
                                    "3 - Comparção dos valores com a media obtida\n"
                                    "Digite o numero do serviço:")
    else:
        continue

    if confirmacao == "2":
        for elem in range (0,len(tickets)):
            soma = soma + tickets[elem]
        media = soma/contador_elementos

    else:
        continue

    print(f"O Valor total das vendas foi de: {soma}")
    print(f"A media dos valores foi de: {media:.2f}\n")
    confirmacao = input("1 - Adicionar Valores de Vendas\n"
                        "2 - Medias dos valores digitados\n"
                        "3 - Comparção dos valores com a media obtida\n"
                        "Digite o numero do serviço:")

    if confirmacao == "3":
      for i in tickets:
        if i < media:
            menor = "menor"
            validacao.append(menor)
        else:
            maior = "maior"
            validacao.append(maior)
    else:
        continue

    print(validacao)
if confirmacao == "0":
        print("Um erro ocorreu, por favor digite o numero do serviço correto!")
        confirmacao = input("1 - Adicionar Valores de Vendas\n"
                                "2 - Medias dos valores digitados\n"
                                "3 - Comparção dos valores com a media obtida\n"
                                "Digite o numero do serviço:")
continue