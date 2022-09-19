def registerNotes(dados: dict):

    print('')
    print('CADASTRAR NOTAS')
    print('Digite \'.\' em diciplina para sair!')
    print('--------------------')

    while True:
        print('')
        disc = input('Disciplina.....: ')
        if disc == '.':

            return dados

        media = int(input('Media anual....: '))
        status = gradeStatus(media)

        dados[disc] = [media, status]



def printDict(dados: dict):

    if dados != {}:
        print('')
        print('DISCIPLINAS | NOTA | STATUS')
        print('--------------------')
        for i in dados:
            print(f'{i} | {dados[i][0]} | {dados[i][1]}')
    else:
        print('materias nao cadastradas!')


def gradeStatus(dados: int):

    if dados >= 6:
        return 'Aprovado'
    return 'Reprovado'



def choice():

    while True:

        try:
            choice = int(input('Opcao desejada: '))
            if choice > 2 or choice < 0:
                raise ValueError
            return choice

        except ValueError:
            print("Por favor digite um numero valido!")



def options():

    print('CADASTRO DISCIPLINAS')
    print('--------------------')
    print('0 - SAIR')
    print('1 - Cadastrar notas')
    print('2 - Listar registro completo')
    print('')


dados = {}

while True:

    options()

    escolha= choice()

    match escolha:

        case 0:
            break

        case 1:
            registerNotes(dados)

        case 2:
            printDict(dados)

