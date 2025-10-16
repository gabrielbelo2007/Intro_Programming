print("Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…")
print('Jamal - "Que danado é isso?"')

monitores_validos = ["Guilherme", "Henrique", "Júnior", "Miguel"]

entrada_valida = False
while not entrada_valida:
    monitores_notas = input().split(", ")
    entrada_valida = True
    
    monitores = []
    for monitor in range(0, len(monitores_notas), 2):
        if monitores_notas[monitor] in monitores_validos and monitores_notas[monitor] not in monitores:
            monitores.append(monitores_notas[monitor])
    
    if len(monitores) != 4:
        print("Insira nomes válidos.")
        entrada_valida = False


# Monitor nota 10
monitor_nota_10 = []
indice_monitor_menor_nota = 1

# Salvar o monitor com a menor nota
for posicao_nota_monitor in range(1, len(monitores_notas), 2):

    if int(monitores_notas[posicao_nota_monitor]) < int(monitores_notas[indice_monitor_menor_nota]):
        indice_monitor_menor_nota = posicao_nota_monitor
    
    # Verificar nota 10
    if monitores_notas[posicao_nota_monitor] == '10' :
        # O monitor está uma posição antes que a sua nota na lista
        monitor_nota_10.append(monitores_notas[posicao_nota_monitor - 1])

monitor_menor_nota = monitores_notas[indice_monitor_menor_nota - 1]

if monitor_nota_10 != []:

    for monitor in monitor_nota_10:
        print(f"O monitor {monitor} é diferenciado! Teve a aprovação do próprio Jamal.")

passinhos_jamal = ["D12", "D33", "E12", "E31", "D12", "E31", "D12"]

print(f"Jamal avaliou a situação dos monitores e viu que {monitor_menor_nota} é o mais necessitado.")
print('Jamal - "Vou ensinar apenas uma vez, então preste atenção."')

# Primeiro jamal se apresenta, e depois o monitor com a menor nota
apresentacoes = 0

# Caso o monitor só tenha errado um passo, ele tem uma segunda chance

passos_dancarino = [passinhos_jamal]
segunda_tentativa = False

while apresentacoes < 2:
    matriz_danca = [
        [".", ".", "."],
        [".", ".", "."],
        ["E", ".", "D"]
    ]
    
    dancarino = "Jamal" if apresentacoes == 0 else f"{monitor_menor_nota}"

    print()
    print(f"{dancarino} - Movimentação 0:")
    for linha_matriz in matriz_danca:
        print(" ".join(linha_matriz))


    # Posição inicial dos pés
    linha_E = 2
    coluna_E = 0

    linha_D = 2
    coluna_D = 2

    for movimento, num_movimentacao in zip(passos_dancarino[apresentacoes], range(len(passinhos_jamal))):
        
        pe = movimento[0]
        linha = int(movimento[1]) - 1
        coluna = int(movimento[2]) - 1

        if pe == "E":
            
            # Caso o pé se mova aonde estava o pé anterior
            if matriz_danca[linha][coluna] == str(num_movimentacao) and matriz_danca[linha_E][coluna_E] != str(num_movimentacao):
                
                linha_D = linha_E
                coluna_D = coluna_E
                
            else:
                matriz_danca[linha_E][coluna_E] = "."
            
            matriz_danca[linha][coluna] = str(num_movimentacao + 1)

            linha_E = linha
            coluna_E = coluna

        else:

            if matriz_danca[linha][coluna] == str(num_movimentacao) and matriz_danca[linha_D][coluna_D] != str(num_movimentacao):
                
                linha_E = linha_D
                coluna_E = coluna_D
            
            else:
                matriz_danca[linha_D][coluna_D] = "."

            matriz_danca[linha][coluna] = str(num_movimentacao + 1)

            linha_D = linha
            coluna_D = coluna

        if pe == "E":
            matriz_danca[linha_D][coluna_D] = "D"
        
        else:
            matriz_danca[linha_E][coluna_E] = "E"

        # Imprimir matriz com movimento atual
        print()
        print(f"{dancarino} - Movimentação {num_movimentacao + 1}:")
        for linha_matriz in matriz_danca:
            print(" ".join(linha_matriz))
            

    # Agora é apresentação do monitor, receber seus passos
    if apresentacoes == 0:
        elementos_permitidos = ["E", "D", "1", "2", "3"]
        errou = 0

        movimentacao_valida = False
        while not movimentacao_valida:

            passinhos_monitor = input().split(", ")
            movimentacao_valida = True  
            
            passos_diferentes = 0
            
            if len(passinhos_monitor) == 7:

                for passo_monitor, passo_jamal in zip(passinhos_monitor, passinhos_jamal):
                    
                    if len(passo_monitor) == 3:
                        for caracter in passo_monitor:
                            if caracter not in elementos_permitidos:
                                movimentacao_valida = False
                            
                        if passo_monitor != passo_jamal:
                            passos_diferentes += 1
                    
                    else:
                        movimentacao_valida = False
                        
            else:
                movimentacao_valida = False
            
            if not movimentacao_valida:
                errou += 1

                if errou == 1:
                    print()
                
                print("Movimento inválido! Por favor, insira outro.")

        if passos_diferentes == 1:
            segunda_tentativa = True

        passos_dancarino.append(passinhos_monitor)
        apresentacoes += 1

    elif segunda_tentativa:
        print()
        print("Foi quase! O monitor merece uma nova chance!")

        segunda_tentativa = False
        passinhos_monitor = input().split(", ")

        passos_dancarino.pop(1)
        passos_dancarino.append(passinhos_monitor)

    else:
        apresentacoes += 1

print()

aprendeu = False
if passos_diferentes == 0:

    if monitor_menor_nota == "Júnior":
        print("Uma máquina! Depois de horas vendo o passinho no Instagram ele conseguiu pegar mais rápido.")

    elif monitor_menor_nota == "Henrique":
        print("O maldito talento ataca novamente! Tinha que ser o desenrolado.")

    elif monitor_menor_nota == "Miguel":
        print("O cara veio do interior pra mostrar como que se faz!")

    elif monitor_menor_nota == "Guilherme":
        print("Ninguém nunca tinha visto ele dançar! Sabíamos que ele estava escondendo um dom.")


elif passos_diferentes == 1:
    if passinhos_jamal == passinhos_monitor:
            print(f"Era isso! {monitor_menor_nota} só estava precisando de um empurrãozinho.")
            aprendeu =  True
        
    else:
        print(f"Nem com outra tentativa {monitor_menor_nota} conseguiu ajeitar isso.")

elif passos_diferentes == 2:
    print(f"Melhor o monitor {monitor_menor_nota} deixar esse negócio de dança pra lá.")

elif passos_diferentes == 3:
    print(f"Isso tá horrível!")

elif passos_diferentes > 3:
    print(f"O monitor {monitor_menor_nota} foi expulso da festa por não saber dançar.")


if passos_diferentes == 0 or aprendeu:
    print('Jamal - "Vocês aprendem rápido! Quero que vocês dancem no meu próximo show!"')

    resposta_convite = input()

    if resposta_convite == "Sim":
        print(f"Óbvio que o monitor {monitor_menor_nota} não perderia essa oportunidade por nada!")
    
    else:
        print(f"Infelizmente o monitor {monitor_menor_nota} jogou essa oportunidade fora. Todos sabem que lá na frente ele vai se arrepender disso.")

else:
    print("Jamal desistiu de ensinar pra quem não aprende. Ele saiu em grande estilo, mandando o passinho e andando.")