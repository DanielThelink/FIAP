dictDisciplinas = {}

#dictDisciplinas["MATEMATICA"] = [8, "APROVADO"]
#dictDisciplinas["PROTGURUES"] = [2, "REPRIOVADO"]
#dictDisciplinas["ESPANHOL"] = [10, "APROVADO"]

mediaAprovacao = 6

def definirAprovado(media):
    if media < mediaAprovacao:
        return "Reprovado"
    else:
        return "Aprovado"

def inputStr(txt):
    return str(input(txt))

def inputInt(txt):
    return int(input(txt))

def inputFloat(txt):
    return float(input(txt))

def cadastrar():

    while True:
        materia = inputStr("Inserir Matéria ou '.' para sair:")
        if (materia == '.'):
            break
        else:
            media = inputFloat(f"Inserir media da matéria {materia}")
            status = definirAprovado(media)
            dictDisciplinas[materia] = [media, status]

# dsa

def cabecalho():
    print("LISTAR DISCIPLINAS")
    print("Disciplinas  |   MF      |   Status\n-----------------------------")

def listar():
        # dictDisciplinas = {'MATEMATICA': [8, 'APROVADO'], 'PROTGURUES': [2, 'REPRIOVADO'], 'ESPANHOL': [10, 'APROVADO']}
        # chave = 'MATEMATICA'
        # valor = [8, 'APROVADO']
        # valor[0] = 8
        # valor[1] = 'APROVADO'

    for chave in dictDisciplinas.keys():
        valor = dictDisciplinas[chave]

        media = valor[0]
        status = valor[1]
        print(f"{chave}     |   {media}     |   {status}")


def mostrarDados():
    cabecalho()
    listar()


def selecionarOpcao():
    while True:
        escolha = mostrarOpcoesMenu()

        if escolha == 1:
            print("Opecao escolhida: cadastrar")
            cadastrar()

        if escolha == 2:
            print("Opecao escolhida: listar")
            mostrarDados()
        if escolha == 0:
            print("Final da execução")
            break

def mostrarOpcoesMenu():
    print("CADASTRO DISCIPLINAS-----------------------------\n"
          "0 - SAIR\n"
          "1 - Cadastrar as disciplinas\n"
          "2 - Listar o registro Completo")
    opcaoEscolhida = int(input("Opção desejada:"))

    return opcaoEscolhida


## Execução principal do código

selecionarOpcao()