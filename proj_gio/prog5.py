#!/usr/bin/pyhon3

nome = "Giovane Fracassi"
print(f"Bem vindo ao Sistemas de e-mails desenvolvido por {nome}")


lista_emails = []
qtd_ativos = 0


def cadastrar_email():
    global qtd_ativos

    while True:
        nome_completo = input("Por favor entre com o Nome Completo do Funcionário: ")
        setor = input("Por favor entre com o Setor do Funcionário: ")

        # Verifica se o funcionário já está cadastrado
        funcionario_existe = False
        for email_dict in lista_emails:
            if email_dict['nome'].lower() == nome_completo.lower():
                funcionario_existe = True
                print(f"Funcionário já está cadastrado. E-mail: {email_dict['email']}")
                break

        if funcionario_existe:
            continue

        # Gerar e-mail
        nomes = nome_completo.split()
        primeiro_nome = nomes[0].lower()
        ultimo_nome = nomes[-1].lower()

        # Começar com a primeira letra do último nome
        sufixo_ultimo_nome = ""
        for i in range(len(ultimo_nome)):
            sufixo_ultimo_nome = ultimo_nome[:i + 1]
            email_gerado = f"{primeiro_nome}.{sufixo_ultimo_nome}@fritadeirastore.com"

            # Verificar se e-mail já existe
            email_existe = False
            for email_dict in lista_emails:
                if email_dict['email'] == email_gerado:
                    email_existe = True
                    break

            if not email_existe:
                break

        # Criar dicionário
        funcionario_dict = {
            'nome': nome_completo,
            'email': email_gerado,
            'setor': setor,
            'ativo': True
        }

        # Copiar dicionário para lista
        lista_emails.append(funcionario_dict.copy())
        qtd_ativos += 1

        print(f"E-mail {email_gerado} cadastrado com sucesso!")
        break


def consultar_emails():
    while True:
        print("\n----------- MENU CONSULTAR E-MAIL -----------")
        print("Qual opção deseja:")
        print("1 - Consultar Todos")
        print("2 - Consultar por Nome de Funcionário")
        print("3 - Consultar por Setor")
        print("4 - Retornar ao menu")

        opcao = input(">>")

        match opcao:
            case '1':
                print("\n--- E-MAILS ATIVOS ---")
                for email_dict in lista_emails:
                    if email_dict['ativo']:
                        print(f"Nome: {email_dict['nome']} - E-mail: {email_dict['email']}")

            case '2':
                nome_busca = input("Digite o nome do funcionário: ")
                encontrado = False
                for email_dict in lista_emails:
                    if email_dict['nome'].lower() == nome_busca.lower():
                        status = "ATIVO" if email_dict['ativo'] else "INATIVO"
                        print(f"Nome: {email_dict['nome']} - E-mail: {email_dict['email']} - Status: {status}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Funcionário não encontrado.")

            case '3':
                setor_busca = input("Digite o setor: ")
                print(f"\n--- E-MAILS ATIVOS DO SETOR {setor_busca.upper()} ---")
                encontrados = False
                for email_dict in lista_emails:
                    if email_dict['setor'].lower() == setor_busca.lower() and email_dict['ativo']:
                        print(f"Nome: {email_dict['nome']} - E-mail: {email_dict['email']}")
                        encontrados = True
                if not encontrados:
                    print("Nenhum funcionário ativo encontrado neste setor.")

            case '4':
                break

            case _:
                print("Opção inválida")


def desativar_email():
    global qtd_ativos

    while True:
        nome_funcionario = input("Digite o nome do funcionário a ter o e-mail desativado: ")

        encontrado = False
        for email_dict in lista_emails:
            if email_dict['nome'].lower() == nome_funcionario.lower():
                if email_dict['ativo']:
                    email_dict['ativo'] = False
                    qtd_ativos -= 1
                    print(f"E-mail de {nome_funcionario} desativado com sucesso!")
                else:
                    print(f"E-mail de {nome_funcionario} já estava desativado.")
                encontrado = True
                break

        if encontrado:
            break
        else:
            print("Funcionário sem E-mail")


def ativar_email():
    global qtd_ativos

    while True:
        nome_funcionario = input("Digite o nome do funcionário a ter o e-mail ativado: ")

        encontrado = False
        for email_dict in lista_emails:
            if email_dict['nome'].lower() == nome_funcionario.lower():
                if not email_dict['ativo']:
                    email_dict['ativo'] = True
                    qtd_ativos += 1
                    print(f"E-mail de {nome_funcionario} ativado com sucesso!")
                else:
                    print(f"E-mail de {nome_funcionario} já estava ativado.")
                encontrado = True
                break

        if encontrado:
            break
        else:
            print("Funcionário sem E-mail")


while True:
    print("\n" + "-" * 50)
    print("-------------- MENU PRINCIPAL ----------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar E-mail")
    print("2 - Consultar E-mail(s)")
    print("3 - Desativar E-mail")
    print("4 - Ativar E-mail")
    print("5 - Encerrar Programa")

    opcao = input(">>")

    match opcao:
        case '1':
            print("\n" + "-" * 50)
            print("---------- MENU CADASTRAR E-MAIL --------------")
            cadastrar_email()

        case '2':
            consultar_emails()

        case '3':
            desativar_email()

        case '4':
            ativar_email()

        case '5':
            print("Programa encerrado!")
            break

        case _:
            print("Opção inválida")
