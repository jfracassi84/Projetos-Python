#!/usr/bin/python3

# Bibliotecas importadas
import sys
import time

# Variável global para acumular o valor total
total_acumulado = 0

# Função de vendas
def venda(sabor, tamanho):
    try:
        if sabor == "CP" and tamanho == "P":
            valor = 9.00
        elif sabor == "CP" and tamanho == "M":
            valor = 14.00
        elif sabor == "CP" and tamanho == "G":
            valor = 18.00
        elif sabor == "AC" and tamanho == "P":
            valor = 11.00
        elif sabor == "AC" and tamanho == "M":
            valor = 16.00
        elif sabor == "AC" and tamanho == "G":
            valor = 20.00
        else:
            return None # Se o valor for nulo, retorna none. Gera a condição "if valor is None"
        return valor
    except:
        print("Sabor ou tamanho inválido! Tente novamente.")


# Função que soma valores acumulados
def acumulador(valor):
    global total_acumulado
    total_acumulado += valor
    return total_acumulado


# Função de menu
def menu():
    nome = "Giovane Fracassi"

    print(f"Bem-vindo a loja de gelados do {nome}")
    print("----------------------Cardápio----------------------")
    print("----------------------------------------------------")
    print("-------| Tamanho | Capuaçu (CP) | Açaí (AC) | ------")
    print("-------|    P    | R$ 9.00      | R$ 11.00  |-------")
    print("-------|    M    | R$ 14.00     | R$ 16.00  |-------")
    print("-------|    G    | R$ 18.00     | R$ 20.00  |-------")
    print("----------------------------------------------------")

    sabor = input("Entre com o sabor desejado (CP/AC): ").upper()
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()

    valor = venda(sabor, tamanho)

    # Condição que se o valor for nulo, retorna None
    # Imprime a mensagem de erro e retorna para o menu
    if valor is None:
        print("Sabor ou tamanho inválidos! Tente novamente.")
        menu()
        return

    print(f"Você pediu um {sabor}, tamanho {tamanho}: R$ {valor:.2f}")

    vl = acumulador(valor)
    print(f"Valor total da compra: {vl:.2f}")

    ent = input("Deseja fazer um novo pedido? [S/N] ").upper()
    if ent == "S":
        menu()
    else:
        print("Saindo do programa...")
        time.sleep(3)
        sys.exit(0)


# Inicio do programa
ent = input("Deseja fazer um novo pedido? [S/N] ").upper()
if ent == "S":
    menu()
else:
    print("Saindo do programa...")
    time.sleep(2)
    sys.exit(0)

