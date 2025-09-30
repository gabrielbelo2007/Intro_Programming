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
        if not andre_saiu:
            if resultado == "acertou":
                bolinhas_andre += 2 if not (bruno_saiu or clara_saiu) else 1
                bolinhas_bruno -= 1 if not bruno_saiu else 0
                bolinhas_clara -= 1 if not clara_saiu else 0
                erros_andre = 0
            else:
                erros_andre += 1
                if erros_andre == 3:
                    print("andre perdeu feio")
                    andre_saiu = True

    elif participante == 1:
        if not bruno_saiu:
            if resultado == "acertou":
                bolinhas_bruno += 2 if not (andre_saiu or clara_saiu) else 1
                bolinhas_andre -= 1 if not andre_saiu else 0
                bolinhas_clara -= 1 if not clara_saiu else 0
                erros_bruno = 0
            else:
                erros_bruno += 1
                if erros_bruno == 3:
                    print("bruno perdeu feio")
                    bruno_saiu = True

    else:
        if not clara_saiu:
            if resultado == "acertou":
                bolinhas_clara += 2 if not (bruno_saiu or andre_saiu) else 1
                bolinhas_bruno -= 1 if not bruno_saiu else 0
                bolinhas_andre -= 1 if not andre_saiu else 0
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
    if not andre_saiu:
        ativos += 1
    if not bruno_saiu:
        ativos += 1
    if not clara_saiu:
        ativos += 1

    if ativos > 1:
        participante = (participante + 1) % 3
        participando = False
        while not participando:
            if participante == 0:
                if andre_saiu == True:
                    participante += 1
                else:
                    participando = True

            elif participante == 1: 
                if bruno_saiu == True:
                    participante += 1
                else:
                    participando = True

            elif participante == 2:   
                if clara_saiu == True:
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