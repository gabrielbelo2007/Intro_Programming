# n também define a quantidade de almas
n = int(input())

# ala = x, lote = y
ala_ocupada = int(input())
lote_ocupado = int(input())

while (ala_ocupada > n or lote_ocupado > n) or (ala_ocupada <= 0 or lote_ocupado <= 0):
    print(f"Rogério e Chaguinha não encontraram o túmulo ocupado na posição {ala_ocupada, lote_ocupado}. Assim eles nunca vão conseguir sair do cemitério!")

    ala_ocupada = int(input())
    lote_ocupado = int(input())

print(f"Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em {ala_ocupada, lote_ocupado}!\n")

# Construção tabuleiro
tabuleiro = []
for ala in range(n):

    # ala_ocupada e lote_ocupado subtraído 1 = index
    if ala != (ala_ocupada - 1):
        tabuleiro.append([0 for lotes in range(n)])
    
    else:
        ala_selada = []

        for lote in range(n):

            if lote == (lote_ocupado - 1):
                ala_selada.append(2)

            else:
                ala_selada.append(0)
                
        tabuleiro.append(ala_selada)


def sem_ameaca(tabuleiro, linha, coluna):

    tam = len(tabuleiro)
    
    # Verificar posição selada
    if tabuleiro[linha][coluna] == 2:
        return False
    
    # Verifica todas as linhas até a última linha que teve uma rainha posicionada
    for ala_1 in range(linha):
        
        if 1 == tabuleiro[ala_1][coluna]:
            return False
        
        lote_1 = tabuleiro[ala_1].index(1)

        ala_2 = linha # ala_atual
        lote_2 = coluna # lote_atual

        if abs(ala_1 - ala_2) == abs(lote_1 - lote_2):
            return False

    # Se posição livre         
    return True
        

# 0 = Casa Livre | 1 = Rainha | 2 = Selo
def posicoes_possiveis(tabuleiro, ala=0):
    
    tam = len(tabuleiro)
    combinacoes = 0

    # Caso base
    if ala == tam:
        return 1
    
    for lote in range(tam):

        if sem_ameaca(tabuleiro, ala, lote):

            tabuleiro[ala][lote] = 1

            combinacoes += posicoes_possiveis(tabuleiro, ala + 1)

            tabuleiro[ala][lote] = 0

    return combinacoes

possibilidades = posicoes_possiveis(tabuleiro)

print(f"Rogério e Chaguinha conseguiram encontrar {possibilidades} possíveis posições para as almas se posicionarem sem conflitos!")

if possibilidades == 0:
    print(f"Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!")

else:
    if possibilidades <= 10:
        print("Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!")

    elif 50 >= possibilidades > 10:
        print("Uau! São tantas opções que eles até se perderam contando!")
    
    else:
        print("Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério.")