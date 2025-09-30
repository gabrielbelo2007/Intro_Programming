ana_ganhou = 0
adrieli_ganhou = 0
joab_ganhou = 0
duda_ganhou = 0

tentativas = int(input())
for jogador in range(4):

    registro_tentativa = False
    for tentativa in range(tentativas):
        ultima_casa = int(input())
        if ultima_casa == 5:
            registro_tentativa = True
    
    if jogador == 0:
        print(f"Ana tentou {tentativas} vezes e completou a última casa {ultima_casa}")
        if registro_tentativa:
            print(f"Ana completou a amarelinha!")
            ana_ganhou = 1
        else:
            print("Ana não conseguiu completar a amarelinha!")
    
    elif jogador == 1:
        print(f"Adrieli tentou {tentativas} vezes e completou a última casa {ultima_casa}")
        if registro_tentativa:
            print(f"Adrieli completou a amarelinha!")
            adrieli_ganhou = 1
        else:
            print("Adrieli não conseguiu completar a amarelinha!")

    
    elif jogador == 2:
        print(f"Joab tentou {tentativas} vezes e completou a última casa {ultima_casa}")
        if registro_tentativa:
            print(f"Joab completou a amarelinha!")
            joab_ganhou = 1
        else:
            print("Joab não conseguiu completar a amarelinha!")

    else: 
        print(f"Duda tentou {tentativas} vezes e completou a última casa {ultima_casa}")
        if registro_tentativa:
            print(f"Duda completou a amarelinha!")
            duda_ganhou = 1
        else:
            print("Duda não conseguiu completar a amarelinha!")


if (ana_ganhou + adrieli_ganhou + joab_ganhou + duda_ganhou) > 1:
    texto = "Houve empate entre:"
    ganhadores = 0

    if ana_ganhou == 1:
        texto += " Ana"
        ganhadores += 1

    if adrieli_ganhou == 1:
        if ganhadores > 0:
            texto += ", Adrieli"
        else:
            texto += " Adrieli"
            ganhadores += 1

    if joab_ganhou == 1:
        if ganhadores > 0:
            texto += ", Joab"
        else:
            texto += " Joab"
    
    if duda_ganhou == 1:
        texto += ", Duda"

    print(texto)

else:
    if ana_ganhou == 1:
        print("O vencedor é Ana!")
    elif adrieli_ganhou == 1:
        print("O vencedor é Adrieli!")
    elif joab_ganhou == 1:
        print("O vencedor é Joab!")
    else:
        print("O vencedor é Duda!")