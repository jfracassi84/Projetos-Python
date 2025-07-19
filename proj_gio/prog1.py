#!/usr/bin/python3

# Bibliotecas importadas
# Bibliotecas para uso do Ctrl+C
import signal
import sys


# Função que captura o Ctrl+C
def signal_handler(sig, frame):
    print("\nVocê pressionou Ctrl+C!")
    sys.exit(0)


# Função que não gera descontos
def semDesconto(vProd, qtd):
    try:
        if vProd < 2500:
            valor = vProd * qtd
            vDesconto = valor * 0.00 #Desconto 0%
        else:
            valor = vProd * qtd
        return valor
    except Exception as error:
        print("Ocorreu um erro!")
        print(error)
    

# Função que gera descontos
def comDesconto(vProd, qtd):
    try:
        if vProd >= 2500 and vProd < 6000:
            valor = vProd * qtd
            vDesconto = valor * 0.04 #Desconto 4%
        elif vProd >= 6000 and vProd < 10000:
            valor = vProd * qtd
            vDesconto = valor * 0.07
        elif vProd >= 10000:
            valor = vProd * qtd
            vDesconto = valor * 0.11
        else:
            if vProd < 1:
                print("Valor Inválido")
        return vDesconto
    except Exception as error:
        print("Ocorreu um erro!")
        print(error)


# Inicio do programa
while True:
    print("=" * 40)
    nome = "Giovane Fracassi"
    print(f"Bem-vindo a loja do {nome}")

    #Chamada da função que captura o Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        print("Programa rodando... Pressione Ctrl+C para sair")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário!")
        sys.exit(0)

    vProd = int(input("Entre com o valor do produto: "))
    qtd = int(input("Entre com a quantidade do produto: "))

    valor_sem_desconto = semDesconto(vProd, qtd)
    valor_com_desconto = comDesconto(vProd, qtd)

    print(f"O valor SEM desconto: {valor_sem_desconto:.2f}")
    print(f"O valor COM desconto: {valor_com_desconto:.2f}")

    