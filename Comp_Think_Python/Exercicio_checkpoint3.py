tickets = []
validacao = []
melhores_valores = []
soma = 0
media = 0
contador_elementos = 0
confirmacao = 78787


while confirmacao != "0":
    print("1 - Adicionar Valores de Vendas\n"
          "2 - Medias dos valores digitados\n"
          "3 - Comparação dos valores com a media obtida\n"
          "4 - Verificar o tícket de maior valor\n"
          "5 - Armazenar em outra lista somente os tickets que superaram a média atual\n")

    confirmacao = (input("Digite o numero do serviço:"))

    if confirmacao == "1":
        addticket = 10
        while addticket != 0:
            addticket = float(input("Adicione os valores das vendas aqui:"))
            tickets.append(addticket)
            contador_elementos += 1
            if addticket == 0:
                tickets.pop()
                contador_elementos = contador_elementos -1

    elif confirmacao == "2":
        for elem in tickets:
            soma = soma + elem
        media = soma/contador_elementos
        print(f"O Valor total das vendas foi de: {soma}")
        print(f"A media dos valores foi de: {media:.2f}\n")

    elif confirmacao == "3":

        for ticket in tickets:
            if ticket > 129.37:
                validacao.append("Superior")
            elif ticket < 129.37:
                validacao.append("Inferior")
            else:
                validacao.append("Igual")
        print(tickets)
        print(validacao)

    elif confirmacao == "4":

        print(f"O valor mais baixo da venda foi de:R$\033[91m{min(tickets)}\033[0m")

        print(f"O valor mais alto da venda foi de:R$\033[92m{max(tickets)}\033[0m")

    elif confirmacao == "5":
    # 7 - armazenar em outra lista somente os tickets que superaram a média atual
        for valor_media in tickets:
            if valor_media > media:
                melhores_valores.append(valor_media)

    print(melhores_valores)
    if confirmacao == "0":
        ...
    else:
        print("Opção invalida, por favor digite a opção correta.")