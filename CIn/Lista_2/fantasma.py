print("Que comece o jogo! Adivinhe a palavra, mas cuidado para não cair na armadilha.")

numero_rodadas = int(input())

for rodada in range(numero_rodadas):
    print(f"Rodada {rodada + 1}/{numero_rodadas}:")

    palavra_secreta = input().lower()

    letras_comum = "aaa"
    while len(letras_comum) >= 3:
        palavra_fantasma = input().lower()

        letras_comum = ""
        for letra in palavra_fantasma:
            if letra in palavra_secreta and letra not in letras_comum:
                letras_comum += letra

        if len(letras_comum) >= 3:
            print(f"A palavra fantasma possui {len(letras_comum)} letras presentes na palavra secreta. Tente uma com menos de 3 letras iguais.")

    vidas = 6
    chutes = ""
    acertos = ""

    letras_certas = ""
    for letra in palavra_secreta:
        if letra not in letras_certas:
            letras_certas += letra

    
    texto = "Palavra: "
    for i in range(len(palavra_secreta)):
        if i < (len(palavra_secreta) - 1):
            texto += "_ "
        else:
            texto += "_"
    print(texto)

    tentativas = 0
    while vidas > 0 and len(acertos) != len(letras_certas):
        tentativas += 1

        chute = input().lower()
        
        if chute in chutes:
            print(f"Você já tentou a letra '{chute}'. Tente outra.")
        else:
            chutes += chute
            if chute in palavra_secreta:
                print(f"Boa! A letra '{chute}' está na palavra.")
                acertos += chute

            elif chute in palavra_fantasma:
                print(f"CUIDADO! A letra '{chute}' é uma armadilha! Você perdeu 2 vidas.")
                vidas -= 2

            else:
                print(f"Naao! A letra '{chute}' não está na palavra. Você perdeu 1 vida.")
                vidas -= 1
        
        if len(acertos) != len(letras_certas):
            texto = "Palavra: "
            for i, letra in zip(range(len(palavra_secreta)), palavra_secreta):
                if letra not in acertos and i < (len(palavra_secreta) - 1):
                    texto += "_ "
                elif letra not in acertos:
                    texto += "_"
                elif i < (len(palavra_secreta) - 1):
                    texto += letra + " "
                else:
                    texto += letra

            print("=====================")
            print(f"{texto}")
            print(f"Vidas restantes: {vidas}")

            letras = ""
            for i, letra in zip(range(len(chutes)), chutes):
                if letra in chutes and i < (len(chutes) - 1):
                    letras += letra + ", "
                else:
                    letras += letra

            print(f"Letras chutadas: {letras}")

            print("=====================")

    if vidas > 0:
        print(f"Parabéns, Adivinho! Você descobriu a palavra secreta: {palavra_secreta.capitalize()}.")
        print(f"Total de tentativas: {tentativas}")
    
    else:
        print(f"Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: {palavra_secreta.capitalize()}.")