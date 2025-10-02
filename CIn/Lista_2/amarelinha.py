ana_ganhou, adrieli_ganhou, joab_ganhou, duda_ganhou = 0, 0, 0, 0

tentativas = int(input())
for jogador in range(4):

    registro_tentativa = False
    for tentativa in range(tentativas):
        ultima_casa = int(input())
        if ultima_casa == 5:
            registro_tentativa = True
    
    if jogador == 0:
        nome = "Ana"
        if registro_tentativa:
            ana_ganhou = 1

    elif jogador == 1:
        nome = "Adrieli"
        if registro_tentativa:
            adrieli_ganhou = 1

    elif jogador == 2:
        nome = "Joab"
        if registro_tentativa:
            joab_ganhou = 1

    else:
        nome = "Duda"
        if registro_tentativa:
            duda_ganhou = 1
    
    print(f"{nome} tentou {tentativas} vezes e completou a última casa {ultima_casa}")
    if registro_tentativa:
        print(f"{nome} completou a amarelinha!")
    else:
        print(f"{nome} não conseguiu completar a amarelinha!")

if (ana_ganhou + adrieli_ganhou + joab_ganhou + duda_ganhou) > 1:
    texto = "Houve empate entre: "
    ganhadores = False

    if ana_ganhou == 1:
        texto += "Ana"
        ganhadores = True

    if adrieli_ganhou == 1:
        if ganhadores > 0:
            texto += ", Adrieli"
        else:
            texto += "Adrieli"
            ganhadores = True

    if joab_ganhou == 1:
        if ganhadores:
            texto += ", Joab"
        else:
            texto += "Joab"
    
    if duda_ganhou == 1:
        texto += ", Duda"

    print(texto)

else:
    nome_ganhador = "Ana" if ana_ganhou == 1 else "Adrieli" if adrieli_ganhou == 1 else "Joab" if joab_ganhou == 1 else "Duda"
    print(f"O vencedor é {nome_ganhador}!")