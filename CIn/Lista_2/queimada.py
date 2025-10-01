print("Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!")

time_atacante = input()
while time_atacante != "Front-End" and time_atacante != "Back-End":
    print("Entrada inválida!")
    time_atacante = input()

ataque_morto = False
defesa_morto = False

vidas_atacantes = 6
vidas_defensores = 6

# 0 -> Atacante | 1 -> Defensor
jogador_atual = 0 

time0 = "Front-End" if time_atacante == "Front-End" else "Back-End"
time1 = "Back-End" if time0 == "Front-End" else "Front-End"

while vidas_atacantes > 0 and vidas_defensores > 0:

    resultado_ataque = input()
    while resultado_ataque != "acertou" and resultado_ataque != "errou":
        print("Entrada inválida!")
        resultado_ataque = input()           

    if jogador_atual == 0:
        if resultado_ataque == "acertou":
            jogador_atual = 1
            vidas_defensores -= 1
            defesa_morto = True

            if ataque_morto:
                vidas_atacantes += 1
                ataque_morto = False
                print(f"O morto do {time0} acertou um jogador!")

            else:
                print(f"{time0} acertou um jogador!")

        else:
            if vidas_atacantes == 6:
                jogador_atual = 1

            else:
                resultado_defesa = input()
                while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                    print("Entrada inválida!")
                    resultado_defesa = input()

                if resultado_defesa == "pegou":
                    jogador_atual = 1
                    ataque_morto = False
                else:
                    ataque_morto = True if ataque_morto == False else False
                    
    else:
        if resultado_ataque == "acertou":
            jogador_atual = 0
            vidas_atacantes -= 1
            ataque_morto = True

            if defesa_morto:
                vidas_defensores += 1
                defesa_morto = False
                print(f"O morto do {time1} acertou um jogador!")

            else:
                print(f"{time1} acertou um jogador!")

        else:
            if vidas_defensores == 6:
                jogador_atual = 0

            else:
                resultado_defesa = input()
                while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                    print("Entrada inválida!")
                    resultado_defesa = input()

                if resultado_defesa == "pegou":
                    jogador_atual = 0
                    defesa_morto = False
                else:
                    # Errei ataque no time -> vai pro morto | Errei ataque no morto -> vai pro time
                    defesa_morto = True if defesa_morto == False else False
    

    if resultado_ataque == "acertou":
        restantes_back = vidas_atacantes if time0 == "Back-End" else vidas_defensores
        restantes_front = vidas_atacantes if restantes_back == vidas_defensores else vidas_defensores

        print(f"Back-End: {restantes_back} dev(s) em campo. | Front-End: {restantes_front} dev(s) em campo.")

if time0 == "Back-End" or time1 == "Back-End" and restantes_back > 0:
    print(f"Vitória do Back-End! Restaram {restantes_back} devs ainda mantendo o servidor de pé!")
else:
    print(f"Vitória do Front-End! Restaram {restantes_front} devs ainda segurando o layout!")