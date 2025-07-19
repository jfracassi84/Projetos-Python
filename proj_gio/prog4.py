#!/usr/bin/python3

nome = "Giovane Fracassi"

lista_livros = []
id_global = 1


def cadastrar_livro():
    global id_global

    print("-" * 50)
    print("-" * 15 + "CADASTRAR LIVRO" + "-" * 15)
    print("-" * 50)

    # Gera automaticamente o ID do livro
    id_livro = id_global

    # Coleta informações do livro
    titulo = input("Título do livro: ").strip()
    autor = input("Autor do livro: ").strip()
    editora = input("Editora: ").strip()
    ano = input("Ano de publicação: ").strip()
    genero = input("Gênero: ").strip()

    # Validação básica
    if not titulo or not autor:
        print("Erro: Título e autor são obrigatórios!")
        return

    # Cria o dicionário do livro
    livro = {
        'id': id_livro,
        'titulo': titulo,
        'autor': autor,
        'editora': editora,
        'ano': ano,
        'genero': genero
    }

    # Adiciona o livro à lista
    lista_livros.append(livro)

    print(f"\n✓ Livro cadastrado com sucesso!")
    print(f"ID: {id_livro}")
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")

    # Incrementa o ID global para o próximo livro
    id_global += 1


def exibir_livro(livro):
    """Função auxiliar para exibir um livro formatado"""
    print(f"ID: {livro['id']}")
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Editora: {livro['editora']}")
    print(f"Ano: {livro['ano']}")
    print(f"Gênero: {livro['genero']}")
    print("-" * 30)


def consultar_livros():
    print("-" * 50)
    print("-" * 15 + "CONSULTAR LIVROS" + "-" * 15)
    print("-" * 50)

    if not lista_livros:
        print("Nenhum livro cadastrado.")
        return

    print("Como deseja consultar?")
    print("1 - Listar todos os livros")
    print("2 - Buscar por ID")
    print("3 - Buscar por título")
    print("4 - Buscar por autor")

    opcao = input(">> ").strip()

    print("-" * 50)

    if opcao == "1":
        # Listar todos os livros
        print("Todos os livros cadastrados:")
        print("-" * 50)
        for livro in lista_livros:
            exibir_livro(livro)

    elif opcao == "2":
        # Buscar por ID
        try:
            id_busca = int(input("Digite o ID do livro: "))
            encontrado = False

            for livro in lista_livros:
                if livro['id'] == id_busca:
                    print("Livro encontrado:")
                    print("-" * 30)
                    exibir_livro(livro)
                    encontrado = True
                    break

            if not encontrado:
                print(f"Nenhum livro encontrado com ID: {id_busca}")

        except ValueError:
            print("Erro: Digite um ID válido (número).")

    elif opcao == "3":
        # Buscar por título
        titulo_busca = input("Digite o título (ou parte do título): ").strip().lower()
        livros_encontrados = []

        for livro in lista_livros:
            if titulo_busca in livro['titulo'].lower():
                livros_encontrados.append(livro)

        if livros_encontrados:
            print(f"Encontrados {len(livros_encontrados)} livro(s):")
            print("-" * 30)
            for livro in livros_encontrados:
                exibir_livro(livro)
        else:
            print(f"Nenhum livro encontrado com título contendo: '{titulo_busca}'")

    elif opcao == "4":
        # Buscar por autor
        autor_busca = input("Digite o nome do autor (ou parte do nome): ").strip().lower()
        livros_encontrados = []

        for livro in lista_livros:
            if autor_busca in livro['autor'].lower():
                livros_encontrados.append(livro)

        if livros_encontrados:
            print(f"Encontrados {len(livros_encontrados)} livro(s):")
            print("-" * 30)
            for livro in livros_encontrados:
                exibir_livro(livro)
        else:
            print(f"Nenhum livro encontrado com autor contendo: '{autor_busca}'")

    else:
        print("Opção inválida!")


def remover_livro():
    print("-" * 50)
    print("-" * 15 + "REMOVER LIVRO" + "-" * 15)
    print("-" * 50)

    if not lista_livros:
        print("Nenhum livro cadastrado.")
        return

    try:
        id_remover = int(input("Digite o ID do livro a ser removido: "))

        for i, livro in enumerate(lista_livros):
            if livro['id'] == id_remover:
                livro_removido = lista_livros.pop(i)
                print(f"✓ Livro '{livro_removido['titulo']}' removido com sucesso!")
                return

        print("Livro não encontrado.")

    except ValueError:
        print("Erro: Digite um ID válido (número).")


def menu():
    while True:
        print("\n" + "-" * 50)
        print(f"Bem-vindo à Livraria do {nome}")
        print("-" * 50)
        print("-" * 15 + "MENU PRINCIPAL" + "-" * 15)
        print("-" * 50)

        print("Escolha a opção desejada: ")
        print("1 - Cadastrar livro")
        print("2 - Consultar livro(s)")
        print("3 - Remover livro")
        print("4 - Sair")

        op = input(">> ").strip()

        if op == "1":
            cadastrar_livro()
        elif op == "2":
            consultar_livros()
        elif op == "3":
            remover_livro()
        elif op == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

        # Pausa para o usuário ver o resultado
        input("\nPressione Enter para continuar...")


# Executa o programa
if __name__ == "__main__":
    menu()