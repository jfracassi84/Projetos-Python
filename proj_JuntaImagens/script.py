from PIL import Image
import os
import argparse


def redimensionar_imagens(img1, img2, orientacao='horizontal'):
    """
    Redimensiona as imagens para que tenham a mesma altura (horizontal) ou largura (vertical)
    """
    if orientacao == 'horizontal':
        # Para layout horizontal, igualar alturas
        altura_min = min(img1.height, img2.height)

        # Calcular novas larguras mantendo proporção
        nova_largura1 = int(img1.width * altura_min / img1.height)
        nova_largura2 = int(img2.width * altura_min / img2.height)

        img1_redim = img1.resize((nova_largura1, altura_min), Image.Resampling.LANCZOS)
        img2_redim = img2.resize((nova_largura2, altura_min), Image.Resampling.LANCZOS)
    else:
        # Para layout vertical, igualar larguras
        largura_min = min(img1.width, img2.width)

        # Calcular novas alturas mantendo proporção
        nova_altura1 = int(img1.height * largura_min / img1.width)
        nova_altura2 = int(img2.height * largura_min / img2.width)

        img1_redim = img1.resize((largura_min, nova_altura1), Image.Resampling.LANCZOS)
        img2_redim = img2.resize((largura_min, nova_altura2), Image.Resampling.LANCZOS)

    return img1_redim, img2_redim


def unir_imagens(caminho_img1, caminho_img2, caminho_saida, orientacao='horizontal', espacamento=10):
    """
    Une duas imagens JPEG em uma única imagem

    Args:
        caminho_img1: Caminho para a primeira imagem (frente)
        caminho_img2: Caminho para a segunda imagem (verso)
        caminho_saida: Caminho onde salvar a imagem unida
        orientacao: 'horizontal' ou 'vertical'
        espacamento: Espaço em pixels entre as imagens
    """

    try:
        # Abrir as imagens
        img1 = Image.open(caminho_img1)
        img2 = Image.open(caminho_img2)

        print(f"Imagem 1: {img1.size} pixels")
        print(f"Imagem 2: {img2.size} pixels")

        # Redimensionar para mesma altura/largura
        img1_redim, img2_redim = redimensionar_imagens(img1, img2, orientacao)

        # Criar nova imagem combinada
        if orientacao == 'horizontal':
            largura_total = img1_redim.width + img2_redim.width + espacamento
            altura_total = img1_redim.height
            nova_img = Image.new('RGB', (largura_total, altura_total), 'white')

            # Colar as imagens
            nova_img.paste(img1_redim, (0, 0))
            nova_img.paste(img2_redim, (img1_redim.width + espacamento, 0))
        else:
            largura_total = img1_redim.width
            altura_total = img1_redim.height + img2_redim.height + espacamento
            nova_img = Image.new('RGB', (largura_total, altura_total), 'white')

            # Colar as imagens
            nova_img.paste(img1_redim, (0, 0))
            nova_img.paste(img2_redim, (0, img1_redim.height + espacamento))

        # Salvar a imagem final
        nova_img.save(caminho_saida, 'JPEG', quality=95)
        print(f"Imagem unida salva em: {caminho_saida}")
        print(f"Dimensões finais: {nova_img.size} pixels")

    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
    except Exception as e:
        print(f"Erro ao processar imagens: {e}")


def main():
    parser = argparse.ArgumentParser(description='Une duas imagens JPEG (frente e verso)')
    parser.add_argument('frente', help='Caminho para a imagem da frente')
    parser.add_argument('verso', help='Caminho para a imagem do verso')
    parser.add_argument('-o', '--output', default='documento_completo.jpg',
                        help='Nome do arquivo de saída (default: documento_completo.jpg)')
    parser.add_argument('--orientacao', choices=['horizontal', 'vertical'],
                        default='horizontal', help='Orientação do layout (default: horizontal)')
    parser.add_argument('--espacamento', type=int, default=10,
                        help='Espaçamento entre as imagens em pixels (default: 10)')

    args = parser.parse_args()

    # Verificar se os arquivos existem
    if not os.path.exists(args.frente):
        print(f"Erro: Arquivo '{args.frente}' não encontrado")
        return

    if not os.path.exists(args.verso):
        print(f"Erro: Arquivo '{args.verso}' não encontrado")
        return

    print(f"Unindo imagens em layout {args.orientacao}...")
    print(f"Frente: {args.frente}")
    print(f"Verso: {args.verso}")
    print(f"Espaçamento: {args.espacamento}px")
    print("-" * 40)

    unir_imagens(args.frente, args.verso, args.output, args.orientacao, args.espacamento)


# Exemplo de uso direto no código (sem linha de comando)
def exemplo_uso():
    """
    Exemplo de como usar a função diretamente no código
    """
    # Substitua pelos caminhos reais das suas imagens
    frente = "documento_frente.jpg"
    verso = "documento_verso.jpg"
    saida = "documento_completo.jpg"

    # Unir horizontalmente
    unir_imagens(frente, verso, saida, orientacao='horizontal', espacamento=20)

    # Ou unir verticalmente
    # unir_imagens(frente, verso, "documento_vertical.jpg", orientacao='vertical', espacamento=15)


if __name__ == "__main__":
    # Para usar por linha de comando, descomente a linha abaixo:
    main()

    # Para testar diretamente no código, descomente a linha abaixo:
    # exemplo_uso()