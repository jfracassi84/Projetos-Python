#!/usr/bin/python3

AGENDA = {}


def mostrar_contatos():
    if len(AGENDA) > 0:
        for contato in AGENDA:
            buscar_contato(contato)
            break
    else:
        print("Agenda vazia")

def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print("-----------------------------------------------------")
    except KeyError:
        print(f"Contato {contato} inexistente!")
    except Exception as error:
        print("Erro desconhecido:", error)
        print()


def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereco do contato: ')
    return telefone, email, endereco
       

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
    'telefone': telefone,
    'email': email,
    'endereco': endereco,
    }

    salvar()

    print()
    print(f"Contato {contato} adicionado | editado com sucesso")
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)

        salvar()

        print()
        print(f"Contato {contato} excluido com sucesso")
        print()
    except KeyError:
        print(f"Contato {contato} inexistente!")
        print()
    except Exception as error:
        print("Erro desconhecido:", error)
        print()


def exportar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato},{telefone},{email},{endereco}\n')
        print('Agenda exportada com sucesso')
    except Exception as error:
        print('Algum erro ocorreu ao exportar contatos')
        print(error)

#.split(',') separa o conteúdo separado em virgula para uma lista. Se deixar em branco (), irá separar nos espaços.
# split serve para separar valores.
#.strip() remove o \n no final da lista, vazio () é para \n, se quiser remover outra coisa, tem de inserir dentro dos parênteses.
# strip serve para remover valores.
def importar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome,telefone,email,endereco)
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except Exception as error:
        print("Algum erro inexperado aconteceu!")
        print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }

        print('Database carregado com sucesso')
        print(f'{len(AGENDA)} contatos carregados') #mas pode usar len(linhas) também. len == length == tamanho.

    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except Exception as error:
        print("Algum erro inexperado aconteceu!")
        print(error)


def imprimir_menu():
    print("-----------------------------------------------------")
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos do CSV')
    print('0 - Fechar agenda')
    print("-----------------------------------------------------")


# Inicio do programa, onde inicia a lógica e executa as funções acima

carregar()

while True:
    imprimir_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        mostrar_contatos()

    elif opcao == "2":
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print("Contato já existente!")
            continue
        except KeyError:
            print(f"Criando o contato {contato}")
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print(f"Editando o contato {contato}")
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('Contato inexistente!')

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '6':
        nome_arquivo = input('Digite o nome do arquivo a ser exportado:')
        exportar_contatos()

    elif opcao == '7':
        nome_arquivo = input('Digite o nome do arquivo a ser importado:')
        importar_contatos(nome_arquivo)

    elif opcao == '0':
        print('Sair do programa')
        break
    else:
        print("Opção inválida!")

