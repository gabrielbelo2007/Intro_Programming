nome_projeto = input()

# Um ternário seria muito extenso
if nome_projeto == "Memória ROM Simples":
    projeto = 0
elif nome_projeto == "Calculadora de 4 bits":
    projeto = 1
elif nome_projeto == "Sequenciador Musical":
    projeto = 2
elif nome_projeto == "Processador de 8 Bits":
    projeto = 3
elif nome_projeto == "Display de Vídeo 8x8":
    projeto = 4
elif nome_projeto == "Supercomputador V13":
    projeto = 5

# Items "exclusivos" de cada projeto, ordem lexicográfica crescente
items_projeto = [
    ["Redstone", "Repetidores", "Tochas de Redstone"], # Memória ROM Simples
    ["Redstone", "Repetidores", "Tochas de Redstone", "Lâmpadas de Redstone"],  # Calculadora de 4 bits
    ["Redstone", "Repetidores", "Blocos de Notas", "Observadores"],   # Sequenciador Musical
    ["Redstone", "Repetidores", "Lâmpadas de Redstone", "Pistões Aderentes"],  # Processador de 8 Bits
    ["Redstone", "Repetidores", "Comparadores", "Pistões"],  # Display de Vídeo 8x8
    ["Redstone", "Repetidores", "Comparadores", "Pistões Aderentes"] # Supercomputador V13
    ]

# Quantidades dos itens de cada projeto
items_qtd_projeto = [
    [256,  64, 128], # Memória ROM Simples
    [512, 128, 64, 256],  # Calculadora de 4 bits
    [1024, 256, 64, 128],   # Sequenciador Musical
    [4096, 1024, 2048, 512],  # Processador de 8 Bits
    [2048, 512, 256, 128],  # Display de Vídeo 8x8
    [8192,  2048, 1024, 1024] # Supercomputador V13
]

items_uteis = []
qtd_items_uteis = []

items_inuteis = []
qtd_items_inuteis = []

projeto_completo = False
while not projeto_completo:

    item_e_quantidade = input()
    if item_e_quantidade != "Construir!":

        # Dividir o número da palavra
        # Dividir o número da palavra
        divisor = 0
        for caracter in range(len(item_e_quantidade) - 1, -1, -1):
            if item_e_quantidade[caracter] == " " and divisor == 0:
                divisor = caracter

        item = item_e_quantidade[:divisor]
        qtd_item = int(item_e_quantidade[divisor + 1:])
        
        if item not in items_projeto[projeto]:
            print(f"Hmm, {item} não parece ser útil para este projeto.")

            if item not in items_inuteis:
                items_inuteis.append(item)
                qtd_items_inuteis.append(qtd_item)

            else:
                posicao = items_inuteis.index(item)
                qtd_items_inuteis[posicao] += qtd_item

        else:

            if item not in items_uteis:
                items_uteis.append(item)
                qtd_items_uteis.append(qtd_item)
            
            else:
                posicao = items_uteis.index(item)
                qtd_items_uteis[posicao] += qtd_item

            if item == "Redstone":
                print(f"Mais redstone! A energia que move o progresso! (+{qtd_item} Redstone)")

            elif item == "Repetidores":
                print(f"Repetidores para garantir que o sinal chegue longe! Perfeito! (+{qtd_item} Repetidores)")

            elif item == "Tochas de Redstone":
                print(f"Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{qtd_item} Tochas de Redstone)")

            elif item == "Lâmpadas de Redstone":
                print(f"Lâmpadas para o display! O resultado vai ficar bem visível. (+{qtd_item} Lâmpadas de Redstone)")

            elif item == "Observadores":
                print(f"Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{qtd_item} Observadores)")

            elif item == "Comparadores":
                print(f"Comparadores para a lógica! A precisão é a alma do negócio. (+{qtd_item} Comparadores)")

            elif item == "Pistões":
                print(f"Pistões para mover as coisas de lugar. Isso vai ser útil! (+{qtd_item} Pistões)")

            elif item == "Pistões Aderentes":
                print(f"Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{qtd_item} Pistões Aderentes)")

            elif item == "Blocos de Notas":
                print(f"Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{qtd_item} Blocos de Notas)")        

    # Relatório
    else: 
        print()

        faltantes = []

        # Checar se os items úteis tem as quantidades mínimas
        for item, index in zip(items_projeto[projeto], range(len(items_qtd_projeto[projeto]))):
            
            if item in items_uteis:
                posicao_qtd_item = items_uteis.index(item)

                if qtd_items_uteis[posicao_qtd_item] < items_qtd_projeto[projeto][index]:
                    faltam = items_qtd_projeto[projeto][index] - qtd_items_uteis[posicao_qtd_item]

                    faltam //= 64
                    if faltam < 1:
                        faltam = 1
                    faltantes.append([faltam, item])
            
            else:
                faltam = items_qtd_projeto[projeto][index] // 64
                faltantes.append([faltam, item])

        # Verifica se o projeto já tem o material necessário
        if len(faltantes) == 0:
            projeto_completo = True
        
        # Imprime items faltando
        else:
            print(f"Ainda não é possível construir o {nome_projeto}! Faltam:")
            print()

            for nome_item in items_projeto[projeto]:

                for item in faltantes:

                    if item[1] == nome_item:
                        print(f"{item[0]} pack(s) de {item[1]}")
            print()

# O projeto foi concluído
print(f"Viniccius13 conseguiu construir o {nome_projeto}! Partiu programar!")
print()
print(f"Para construirmos a(o) {nome_projeto}, utilizamos:")
print()

for item, qtd_item in zip(items_uteis, qtd_items_uteis):
    print(f"{item} : {qtd_item}")

if (len(items_inuteis) > 0):
    print()
    print(f"Mas, em nossa jornada, também coletamos:")
    print()

    for item, qtd_item in zip(items_inuteis, qtd_items_inuteis):
        print(f"{item} : {qtd_item}")