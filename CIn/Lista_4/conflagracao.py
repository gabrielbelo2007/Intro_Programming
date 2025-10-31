def calculo_distancia(posicao_sam, posicao_analisada):

    resultado = 0
    
    for coordenada_1, coordenada_2 in zip(posicao_sam, posicao_analisada):
        
        distancia = abs(coordenada_1 - coordenada_2)

        resultado = max(resultado, distancia)

    return resultado


def atirar_sam(arma, neil, posicao_sam, posicao_neil):
    
    distancia = calculo_distancia(posicao_sam, posicao_neil)

    dano = 0
    if arma == "Rifle":

        if distancia == 3:
            dano = 15
        
        else:
            dano = 5

    elif arma == "Espingarda":

        if distancia <= 2:
            dano = 25

    elif arma == "Metralhadora":

        if distancia >= 4:
            dano = 15 
    
    neil[0] -= dano

    if dano > 0:
        return True
    return False


def imprimir_matriz(matriz):

    for linha in matriz:
        print(" ".join(linha))


def teletransporte_neil(matriz, sam, posicao_atual, casa_anterior):
    
    maior_distancia = 0
    ponto_final = []

    for linha in range(6):
        for coluna in range(6):

            if matriz[linha][coluna] != "I":
                ponto_analisado = [linha, coluna]

                possivel_distancia = calculo_distancia(sam, ponto_analisado)

                if possivel_distancia >= maior_distancia:
                    maior_distancia = possivel_distancia
                    ponto_final = [linha, coluna]

    # Verificando se ele já está na casa mais distante
    if posicao_atual != ponto_final:
        
        # Alterando a posição atual do Neil para o valor da casa anterior a presença dele
        matriz[posicao_atual[0]][posicao_atual[1]] = casa_anterior[0]
        casa_anterior[0] = matriz[ponto_final[0]][ponto_final[1]]

        # Colocando o Neil na nova posição e salvando o valor da casa que ele ocupou
        posicao_atual[0], posicao_atual[1] = ponto_final[0], ponto_final[1]
        matriz[posicao_atual[0]][posicao_atual[1]] = "N"
    

def movimentacao_sam(movimento, matriz, posicao_atual, casa_anterior):
    
    # posicao_atual[0] = x (linha) | posicao_atual[1] = y (coluna)

    # 0 - Eixo da movimentação | 1 - Variação da Posição
    mudanca_movimento = ["", 0]
    locais_bloqueados = ["I", "N"]

    if movimento == "W":    

        if posicao_atual[0] - 1 >= 0:

            if matriz[posicao_atual[0] - 1][posicao_atual[1]] not in locais_bloqueados: 
                mudanca_movimento[0] = "X"
                mudanca_movimento[1] = -1

    elif movimento == "S":

        if posicao_atual[0] + 1 <= 5:

            if matriz[posicao_atual[0] + 1][posicao_atual[1]] not in locais_bloqueados:
                mudanca_movimento[0] = "X"
                mudanca_movimento[1] = 1

    elif movimento == "A":

        if posicao_atual[1] - 1 >= 0:
            
            if matriz[posicao_atual[0]][posicao_atual[1] - 1] not in locais_bloqueados:
                mudanca_movimento[0] = "Y"
                mudanca_movimento[1] = -1

    elif movimento == "D":

        if posicao_atual[1] + 1 <= 5:

            if matriz[posicao_atual[0]][posicao_atual[1] + 1] not in locais_bloqueados:
                mudanca_movimento[0] = "Y"
                mudanca_movimento[1] = 1
        
    # Verificar se o movimento estava dentro da matriz ou não era Intrasponível

    if mudanca_movimento[0] != "":

        # Alterando a posição atual do Sam para o valor da casa anterior a presença dele
        matriz[posicao_atual[0]][posicao_atual[1]] = casa_anterior[0]

        # Fazendo a variação na posição
        if mudanca_movimento[0] == "X":
            posicao_atual[0] += mudanca_movimento[1]
        
        elif mudanca_movimento[0] == "Y":
            posicao_atual[1] += mudanca_movimento[1]
        
        # Registrando a próxima casa ocupada
        casa_anterior[0] = matriz[posicao_atual[0]][posicao_atual[1]]

        # Movendo Sam
        matriz[posicao_atual[0]][posicao_atual[1]] = "S"

        # Retorna True para caso de casa com fogo
        if casa_anterior[0] == "F":
            return True
        return False


vida_sam = [100]
vida_neil = [100]

arma_atual = "Rifle"

hits_fogo = 0

local_sam = []
local_neil = []

posicao_anterior_sam = ["P"]
posicao_anterior_neil = ["P"]

mapa = []
for num_linha in range(6):
    linha = input().split(" ")

    for casa in linha:
        num_coluna = linha.index(casa)

        if casa == "S":
            local_sam.append(num_linha)
            local_sam.append(num_coluna)

        elif casa == "N":
            local_neil.append(num_linha)
            local_neil.append(num_coluna)

    mapa.append(linha)


print("Sam: Mas que lugar é esse aqui?")
print(f"Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!\n")

movimentos = ["W", "A", "S", "D"]
contagem_acoes = 0
hits_neil = 0

situacao_critica = False  # Flag para 40 de vida ou menos
casa_incediada = False

while vida_sam[0] > 0 and vida_neil[0] > 0:
    
    if casa_incediada:
        hits_fogo += 1
        vida_sam[0] -= 5

    if vida_sam[0] > 0:
        acao = input()

        if acao in movimentos:  
            dano_fogo = movimentacao_sam(acao, mapa, local_sam, posicao_anterior_sam)

            if dano_fogo:
                casa_incediada = True
            
            else:
                casa_incediada = False

        elif acao == "Atirar":
            acertou = atirar_sam(arma_atual, vida_neil, local_sam, local_neil)

            if acertou:
                hits_neil += 1

            if hits_neil == 3 and vida_neil[0] > 0:
                hits_neil = 0
                teletransporte_neil(mapa, local_sam, local_neil, posicao_anterior_neil)
                imprimir_matriz(mapa)

        # Ação: trocar de arma
        else:
            arma_atual = acao
            print(f"Arma trocada para {arma_atual}.")

        if vida_neil[0] > 0:
            contagem_acoes += 1

            if contagem_acoes == 4:
                contagem_acoes = 0
                vida_sam[0] -= 15
                print(">>> Você recebe um disparo de Neil! <<<")

            if vida_sam[0] <= 40 and not situacao_critica:
                print("Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.")
                situacao_critica = True

print()

# Tira o dano recebido pelo fogo e verifica quanto de dano Neil deu
dano_neil = 100 - (hits_fogo * 5 + vida_sam[0])

likes = 1000 - (dano_neil * 8) - (hits_fogo * 10)

if vida_sam[0] > 0:
    print("MISSÃO COMPLETA! - Investigue a Anomalia")
    print("========================================")
    print(f"Likes recebidos: 👍 {likes}")

else:
    print("MISSÃO FALHOU")
    print("==============")
    print("Sam foi derrotado.")
    print("[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")