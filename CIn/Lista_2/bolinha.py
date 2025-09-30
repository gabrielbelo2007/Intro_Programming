bolinhas_andre = int(input())
bolinhas_bruno = int(input())
bolinhas_clara = int(input())

erros_andre = 0
erros_bruno = 0
erros_clara = 0

andre_saiu = False
bruno_saiu = False
clara_saiu = False

ativos = 3
participante = 0

while ativos > 1:
    resultado = input()

    if participante == 0:
        if bolinhas_andre > 0 and erros_andre != 3:
            if resultado == "acertou":
                bolinhas_andre += 1
                bolinhas_bruno -= 1 if bolinhas_bruno > 0 else 0
                bolinhas_clara -= 1 if bolinhas_clara > 0 else 0
                erros_andre = 0
            else:
                erros_andre += 1
                if erros_andre == 3:
                    print("andre perdeu feio")
                    andre_saiu = True

    elif participante == 1:
        if bolinhas_bruno > 0 and erros_bruno != 3:
            if resultado == "acertou":
                bolinhas_bruno += 1
                bolinhas_andre -= 1 if bolinhas_andre > 0 else 0
                bolinhas_clara -= 1 if bolinhas_clara > 0 else 0
                erros_bruno = 0
            else:
                erros_bruno += 1
                if erros_bruno == 3:
                    print("bruno perdeu feio")
                    bruno_saiu = True

    else:
        if bolinhas_clara > 0 and erros_clara != 3:
            if resultado == "acertou":
                bolinhas_clara += 1
                bolinhas_bruno -= 1 if bolinhas_bruno > 0 else 0
                bolinhas_andre -= 1 if bolinhas_andre > 0 else 0
                erros_clara = 0
            else:
                erros_clara += 1
                if erros_clara == 3:
                    print("clara perdeu feio")
                    clara_saiu = True

    if bolinhas_andre == 0 and not andre_saiu:
        print("andre saiu do jogo")
        andre_saiu = True

    if bolinhas_bruno == 0 and not bruno_saiu:
        print("bruno saiu do jogo")
        bruno_saiu = True

    if bolinhas_clara == 0 and not clara_saiu:
        print("clara saiu do jogo")
        clara_saiu = True

    ativos = 0
    if bolinhas_andre > 0 and erros_andre != 3:
        ativos += 1
    if bolinhas_bruno > 0 and erros_bruno != 3:
        ativos += 1
    if bolinhas_clara > 0 and erros_clara != 3:
        ativos += 1

    if ativos > 2:
        participante = (participante + 1) % 3
        participando = False
        while not participando:
            if participante == 0 and andre_saiu == True:
                participante += 1
            else:
                participando = True

            if participante == 1 and bruno_saiu == True:
                participante += 1
            else:
                participando = True

            if participante == 2 and clara_saiu == True:
                participante = 0
            else:
                participando = True

if bolinhas_andre > bolinhas_bruno and bolinhas_andre > bolinhas_clara and erros_andre != 3:
    print("andre ganhou")

elif bolinhas_bruno > bolinhas_andre and bolinhas_bruno > bolinhas_clara and erros_bruno != 3:
    print("bruno ganhou")

else:
    print("clara ganhou")

print("a quantidade final de bolas foi:")
print(f"andre: {bolinhas_andre}")
print(f"bruno: {bolinhas_bruno}")
print(f"clara: {bolinhas_clara}")