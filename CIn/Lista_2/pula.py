print("INICIANDO SIMULAÇÃO...")

jogador1 = input()
while jogador1 != "Samuel" and jogador1 != "Arthur":
    print("Jogador inválido! Essa competição é apenas entre Arthur e Samuel!")
    jogador1 = input()

print(f"{jogador1} começa na corda!")

jogador2 = "Arthur" if jogador1 == "Samuel" else "Samuel"
qtd_rodadas = int(input())

pts_jogador1 = 0
pts_jogador2 = 0

jogador_atual = 0
for rodada in range(qtd_rodadas):
    ritmo = int(input())
    aposta = int(input())

    if jogador_atual > 0:
        jogador_temp = jogador1

        jogador1 = jogador2
        jogador2 = jogador_temp

    print(f"Começa a {rodada + 1}ª rodada!")
    ultima_rodada = (rodada + 1) == qtd_rodadas

    if ultima_rodada:
        print("Última rodada! Valendo 2 pontos!")
    
    print(f"{jogador2} aposta que {jogador1} não chega a {aposta} pulos! Vamos ver se é verdade! O ritmo de {jogador1} será {ritmo}!")

    tropecos = 0
    pulos = 0
    while tropecos < 3 and pulos < aposta:
        pulos_restantes = aposta - pulos

        n = 0
        for digito in str(pulos_restantes):
                n += int(digito)
        
        fibonacci1 = 5 * n**2 + 4
        fibonacci2 = 5 * n**2 - 4

        if (fibonacci1**0.5) % 1 == 0 or (fibonacci2**0.5) % 1 == 0:
            print(f"O número da soma é {n}, que faz parte da sequência de Fibonacci!! {jogador1} tropeça!")
            tropecos += 1

        elif tropecos < 3:
            if pulos > aposta * 0.75 and pulos <= (aposta * 0.75) + ritmo:
                print(f"{jogador1} está quase chegando ao apostado! Falta pouco!")
                
            else:
                print(f"{jogador1} pula com maestria! Faltam {pulos_restantes} pulos!")
        
        pulos += ritmo
    
    if tropecos == 3:
        print(f"E agora não tem jeito, {jogador1} cai de cara no chão!")

    if pulos < aposta:
        if pulos < aposta // 2:
            print(f"Nossa!! Parece que {jogador1} não chegou nem na metade do apostado! Ainda bem que não foi competir pra valer no Round 6!")
            
        elif pulos > aposta // 2 and pulos < aposta * 0.75:
            print(f"Nem muito perto, nem muito longe do apostado. Talvez {jogador1} teve apenas azar!")

        else:
            print(f"Quase lá! por pouco {jogador1} não alcançou o apostado!")

    elif tropecos < 3: 
        if pulos == aposta:
            print(f"{jogador1} cumpriu o prometido e alcançou {aposta} pulos! Ponto merecidíssimo!")

        else:
            print(f"{jogador1} vai além, e supera a aposta em {pulos - aposta} Ponto(s)! Deixou o {jogador2} no chinelo!")

        if jogador_atual == 1:
            pts_jogador1 += 2 if ultima_rodada else 1
        else:
            pts_jogador2 += 2 if ultima_rodada else 1

    jogador_atual += 1

if jogador_atual >= 1 and jogador_atual % 2 != 0:
    jogador_temp = jogador1

    jogador1 = jogador2
    jogador2 = jogador_temp

print("COMPUTANDO PREVISÃO FINAL...")

if pts_jogador1 == 0 and pts_jogador2 == 0:
    print("Ninguém pontuou! Que competição sem graça! Acho que os monitores se garantem mais nas dúvidas de IP mesmo...")

elif pts_jogador1 == pts_jogador2:
    print(f"Houve um empate técnico! Ambos fizeram {pts_jogador1} ponto(s)! Óbvio que os dois monitores mais rápidos iriam empatar!")

elif (jogador1 == "Arthur" and pts_jogador1 > pts_jogador2) or (jogador2 == "Arthur" and pts_jogador2 > pts_jogador1):
    pontos_arthur = pts_jogador1 if pts_jogador1 > pts_jogador2 else pts_jogador2
    print(f"Arthur venceu a competição com {pontos_arthur} ponto(s)! Trouxe orgulho para Maceió!")

elif (jogador1 == "Samuel" and pts_jogador1 > pts_jogador2) or (jogador2 == "Samuel" and pts_jogador2 > pts_jogador1):
    pontos_samuel = pts_jogador1 if pts_jogador1 > pts_jogador2 else pts_jogador2
    print(f"Samuel venceu a competição com {pontos_samuel} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!")
