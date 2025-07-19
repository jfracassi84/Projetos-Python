#!/usr/bin/python3

#Variáveis
# Valores por página
dig = 1.10
ico = 1.00
ipb = 0.40
fot = 0.20


# Função que calcula valores do DIG
def calcularDIG(pag):
    # Verifica se a quantidade de páginas é válida
    global vServico
    global vBase
    global desc
    global tipo_encad
    global extra

    if pag >= 20000:
        print("Não aceitamos pedidos com 20000 páginas ou mais.")
        return None

    # Calcula o valor base sem desconto
    vBase = pag * dig

    # Aplica descontos conforme a quantidade de páginas
    if pag < 20:
        desc = 0 # Sem desconto
        vServico = vBase
    elif pag >= 20 and pag < 200:
        desc = 15 # 15% de desconto
        vServico = vBase * 0.85
    elif pag >= 200 and pag < 2000:
        desc = 20 # 20% de desconto
        vServico = vBase * 0.80
    elif pag >= 2000 and pag <20000:
        desc = 25 # 25% de desconto
        vServico = vBase * 0.75
    else:
        pass

    print(f"Valor sem desconto: R$ {vBase:.2f}")
    if desc > 0:
        print(f"Desconto aplicado: {desc}%")
        print(f"Valor com desconto: R$ {vServico:.2f}")

    # Calcula o valor extra da encadernação
    print("\nOpções de encadernação:")
    print("0 - Não quero encadernação")
    print("1 - Encadernação simples (+R$ 15,00)")
    print("2 - Encadernação capa dura (+R$ 40,00)")

    while True:
        try:
            encadernacao = int(input("Escolha uma opção (0/1/2): "))
            if encadernacao in [0, 1, 2]:
                break
            else:
                print("Opção inválida! Escolha 0, 1 ou 2.")
        except ValueError:
            print("Por favor, digite um número válido!")

    if encadernacao == 0:
        extra = 0
        tipo_encad = "Sem encadernação"
    elif encadernacao == 1:
        extra = 15.00
        tipo_encad = "Encadernação simples"
    elif encadernacao == 2:
        extra = 40.00
        tipo_encad = "Encadernação capa dura"

    # Calcula o total final
    total = vServico + extra

    print(f"\nResumo do pedido:")
    print(f"Páginas: {pag}")
    print(f"Serviço: R$ {vServico:.2f}")
    print(f"Extra ({tipo_encad}): R$ {extra:.2f}")

    return total


# Função que calcula os valores do ICO
def calcularICO(pag):
    # Verifica se a quantidade de páginas é válida
    global vServico, extra
    global vBase
    global desc
    global tipo_encad

    if pag >= 20000:
        print("Não aceitamos pedidos com 20000 páginas ou mais.")
        return None

    # Calcula o valor base sem desconto
    vBase = pag * ico

    # Aplica descontos conforme a quantidade de páginas
    if pag < 20:
        desc = 0 # Sem desconto
        vServico = vBase
    elif pag >= 20 and pag < 200:
        desc = 15 # 15% de desconto
        vServico = vBase * 0.85
    elif pag >= 200 and pag < 2000:
        desc = 20 # 20% de desconto
        vServico = vBase * 0.80
    elif pag >= 2000 and pag <20000:
        desc = 25 # 25% de desconto
        vServico = vBase * 0.75
    else:
        pass

    print(f"Valor sem desconto: R$ {vBase:.2f}")
    if desc > 0:
        print(f"Desconto aplicado: {desc}%")
        print(f"Valor com desconto: R$ {vServico:.2f}")

    # Calcula o valor extra da encadernação
    print("\nOpções de encadernação:")
    print("0 - Não quero encadernação")
    print("1 - Encadernação simples (+R$ 15,00)")
    print("2 - Encadernação capa dura (+R$ 40,00)")

    while True:
        try:
            encadernacao = int(input("Escolha uma opção (0/1/2): "))
            if encadernacao in [0, 1, 2]:
                break
            else:
                print("Opção inválida! Escolha 0, 1 ou 2.")
        except ValueError:
            print("Por favor, digite um número válido!")

    if encadernacao == 0:
        extra = 0
        tipo_encad = "Sem encadernação"
    elif encadernacao == 1:
        extra = 15.00
        tipo_encad = "Encadernação simples"
    elif encadernacao == 2:
        extra = 40.00
        tipo_encad = "Encadernação capa dura"

    # Calcula o total final
    total = vServico + extra

    print(f"\nResumo do pedido:")
    print(f"Páginas: {pag}")
    print(f"Serviço: R$ {vServico:.2f}")
    print(f"Extra ({tipo_encad}): R$ {extra:.2f}")

    return total


# Função que calcula o IPB
def calcularIPB(pag):
    # Verifica se a quantidade de páginas é válida
    global vServico, extra
    global vBase
    global desc
    global tipo_encad

    if pag >= 20000:
        print("Não aceitamos pedidos com 20000 páginas ou mais.")
        return None

    # Calcula o valor base sem desconto
    vBase = pag * ipb

    # Aplica descontos conforme a quantidade de páginas
    if pag < 20:
        desc = 0 # Sem desconto
        vServico = vBase
    elif pag >= 20 and pag < 200:
        desc = 15 # 15% de desconto
        vServico = vBase * 0.85
    elif pag >= 200 and pag < 2000:
        desc = 20 # 20% de desconto
        vServico = vBase * 0.80
    elif pag >= 2000 and pag <20000:
        desc = 25 # 25% de desconto
        vServico = vBase * 0.75
    else:
        pass

    print(f"Valor sem desconto: R$ {vBase:.2f}")
    if desc > 0:
        print(f"Desconto aplicado: {desc}%")
        print(f"Valor com desconto: R$ {vServico:.2f}")

    # Calcula o valor extra da encadernação
    print("\nOpções de encadernação:")
    print("0 - Não quero encadernação")
    print("1 - Encadernação simples (+R$ 15,00)")
    print("2 - Encadernação capa dura (+R$ 40,00)")

    while True:
        try:
            encadernacao = int(input("Escolha uma opção (0/1/2): "))
            if encadernacao in [0, 1, 2]:
                break
            else:
                print("Opção inválida! Escolha 0, 1 ou 2.")
        except ValueError:
            print("Por favor, digite um número válido!")

    if encadernacao == 0:
        extra = 0
        tipo_encad = "Sem encadernação"
    elif encadernacao == 1:
        extra = 15.00
        tipo_encad = "Encadernação simples"
    elif encadernacao == 2:
        extra = 40.00
        tipo_encad = "Encadernação capa dura"

    # Calcula o total final
    total = vServico + extra

    print(f"\nResumo do pedido:")
    print(f"Páginas: {pag}")
    print(f"Serviço: R$ {vServico:.2f}")
    print(f"Extra ({tipo_encad}): R$ {extra:.2f}")

    return total


# Função que calcula o FOT
def calcularFOT(pag):
    # Verifica se a quantidade de páginas é válida
    global vServico, extra
    global vBase
    global desc
    global tipo_encad

    if pag >= 20000:
        print("Não aceitamos pedidos com 20000 páginas ou mais.")
        return None

    # Calcula o valor base sem desconto
    vBase = pag * fot

    # Aplica descontos conforme a quantidade de páginas
    if pag < 20:
        desc = 0 # Sem desconto
        vServico = vBase
    elif pag >= 20 and pag < 200:
        desc = 15 # 15% de desconto
        vServico = vBase * 0.85
    elif pag >= 200 and pag < 2000:
        desc = 20 # 20% de desconto
        vServico = vBase * 0.80
    elif pag >= 2000 and pag <20000:
        desc = 25 # 25% de desconto
        vServico = vBase * 0.75
    else:
        pass

    print(f"Valor sem desconto: R$ {vBase:.2f}")
    if desc > 0:
        print(f"Desconto aplicado: {desc}%")
        print(f"Valor com desconto: R$ {vServico:.2f}")

    # Calcula o valor extra da encadernação
    print("\nOpções de encadernação:")
    print("0 - Não quero encadernação")
    print("1 - Encadernação simples (+R$ 15,00)")
    print("2 - Encadernação capa dura (+R$ 40,00)")

    while True:
        try:
            encadernacao = int(input("Escolha uma opção (0/1/2): "))
            if encadernacao in [0, 1, 2]:
                break
            else:
                print("Opção inválida! Escolha 0, 1 ou 2.")
        except ValueError:
            print("Por favor, digite um número válido!")

    if encadernacao == 0:
        extra = 0
        tipo_encad = "Sem encadernação"
    elif encadernacao == 1:
        extra = 15.00
        tipo_encad = "Encadernação simples"
    elif encadernacao == 2:
        extra = 40.00
        tipo_encad = "Encadernação capa dura"

    # Calcula o total final
    total = vServico + extra

    print(f"\nResumo do pedido:")
    print(f"Páginas: {pag}")
    print(f"Serviço: R$ {vServico:.2f}")
    print(f"Extra ({tipo_encad}): R$ {extra:.2f}")

    return total


# Função para o menu de serviços
def escolha_servico(total=None):
    nome = "Giovane Fracassi"
    print(f"Bem-vindo a copiadora do {nome}")
    print()
    print("Serviços disponíveis: ")
    print("DIG - Digitalização")
    print("ICO - Impressão Colorida")
    print("IPB - Impressão em Preto e Branco")
    print("FOT - Fotocópia")
    serv = input("Entre com o tipo de serviço desejado: ").upper()

    if serv == "DIG":
        pag = int(input("Entre com o número de páginas: "))
        val = calcularDIG(pag)
        if val is not None:  # Só mostra o total se o pedido for válido
            print(f"\nTOTAL FINAL: R$ {val:.2f}")
        else:
            print("Pedido não realizado.")
    elif serv == "ICO":
        pag = int(input("Entre com o número de páginas: "))
        val = calcularICO(pag)
        if val is not None:  # Só mostra o total se o pedido for válido
            print(f"\nTOTAL FINAL: R$ {val:.2f}")
        else:
            print("Pedido não realizado.")
    elif serv == "IPB":
        pass
    elif serv == "FOT":
        pass
    else:
        print("Escolha inválida, entre com o tipo do serviço novamente.")

# Inicio do programa, onde chama o menu de serviços
escolha_servico()
