def distancia(posicao_sam, posicao_analisada):

    resultado = 0
    
    for coordenada_sam, coordenada_analisada in zip(posicao_sam, posicao_analisada):
        
        distancia = abs(coordenada_sam - coordenada_analisada)

        resultado = max(resultado, distancia)

    return resultado

def atirar_sam(arma, neil):
    pass


def teletransporte_neil(matriz, posicao_atual, sam, posicao_anterior):
    
    movimentos = distancia(sam, posicao_atual)


def movimentacao_sam(movimento, matriz, posicao_atual, posicao_anterior):
    pass


vida_sam = [100]
vida_neil = [100]

arma_atual = "Rifle"

hits_fogo = 0
dano_neil = 0

local_sam = []
local_neil = []

posicao_anterior_sam = []
posicao_anterior_neil = []

mapa = []
for num_linha in range(6):
    linha = input().split(" ")

    for posicao in linha:
        num_coluna = linha.index(posicao)

        if posicao == "S":
            local_sam.append(num_linha)
            local_sam.append(num_coluna)

        elif posicao == "N":
            local_neil.append(num_linha)
            local_neil.append(num_coluna)

    mapa.append(linha)


print("Sam: Mas que lugar é esse aqui?")
print(f"Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!\n")

movimentos = ["A", "B", "C", "D"]
contagem_acoes = 0
hits_neil = 0

situacao_critica = False  # Flag para 40 de vida ou menos
while vida_sam > 0 and vida_neil > 0:
    acao = input()

    if acao in movimentos:  
        movimentacao_sam(acao, mapa)

    elif acao == "Atirar":
        atirar_sam(arma_atual, vida_neil)
        hits_neil += 1

        if hits_neil == 3:
            hits_neil = 0
            teletransporte_neil(mapa)

    else:
        arma_atual = acao

    contagem_acoes += 1

    if contagem_acoes == 4:
        contagem_acoes = 0
        vida_sam -= 15
        print(">>> Você recebe um disparo de Neil! <<<")

    if vida_sam <= 40 and not situacao_critica:
        print("Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.")
        situacao_critica = True

print()
likes = 1000 - (dano_neil * 8) - (hits_fogo * 10)

if vida_sam > 0:
    print("MISSÃO COMPLETA! - Investigue a Anomalia")
    print("========================================")
    print(f"Likes recebidos: 👍 {likes}")

else:
    print("MISSÃO FALHOU")
    print("==============")
    print("Sam foi derrotado.")
    print("[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")