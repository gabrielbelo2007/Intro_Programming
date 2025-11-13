# n também define a quantidade de almas
n = int(input())

# ala = x, lote = y
ala_ocupada = int(input())
lote_ocupado = int(input())

tabuleiro = []

for ala in range(n):
    
    if ala != ala_ocupada:
        tabuleiro.append([0 for lotes in range(n)])
    
    else:
        ala_selada = []

        for lote in range(n):

            if lote == lote_ocupado:
                ala_selada.append(2)

            else:
                ala_selada.append(0)
                
        tabuleiro.append(ala_selada)


def sem_ameaca(tabuleiro, posicao):

    tam = len(tabuleiro)

    # Verifica se tem uma rainha na ala(linha)
    if 1 in tabuleiro[posicao[0]]:
        return False
    
    for ala in range(tam):

        # Verifica se tem uma rainha no lote(coluna)
        if 1 == tabuleiro[ala][posicao[1]]:
            return False
        
        if 1 in tabuleiro[ala]:

            ala_1 = ala
            lote_1 = tabuleiro[ala].index(1)

            ala_2 = posicao[0]
            lote_2 = posicao[1]

            if abs(ala_1 - ala_2) == abs(lote_1 - lote_2):
                return False
            
    return True
        

# 0 = Casa Livre | 1 = Rainha | 2 = Selo
def posicoes_possiveis(tabuleiro, posicao=[0,0]):
    
    borda = len(tabuleiro)

    # Caso base (talvez errado)
    # if posicao[0] == borda:
    #     return 1
    
    while not sem_ameaca(tabuleiro, posicao):
        posicao[1] += 1 

        if posicao[1] == len(tabuleiro):
            return 0

    tabuleiro[posicao[0]][posicao[1]] = 1

    posicoes_possiveis(tabuleiro)
