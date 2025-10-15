num_convidados = int(input())

convidados = []
comidas = []
valores_comidas = []

for convidado in range(num_convidados):
    nome_convidado = input()
    comida_convidado = input()
    valor_comida = int(input())
    
    
    if nome_convidado == "Maicon Kuster":
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    elif comida_convidado in comidas:
        print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {nome_convidado}")
    
    else:
        convidados.append(nome_convidado)
        comidas.append(comida_convidado)
        valores_comidas.append(valor_comida) 

if len(convidados) == 0:
    print("Nenhum convidado marcou presença na festa do calabreso!")

else:
    
    # ORDENANDO O VALOR DAS COMIDAS - crie uma lista com a posição (da lista de comidas_valores original) dos valores ordenados para depois utilizar na lista de convidados

    valores_comida_temp = valores_comidas.copy()
    valores_comidas_ordenado = sorted(valores_comidas)

    indice_comidas_ordenado = []
    qtd_comida = len(valores_comidas)
    
    # A lista temporaria é pela limitação do .index() de pegar apenas a posição do primeiro valor
    for index in range(qtd_comida):
        posicao_atual = valores_comida_temp.index(valores_comidas_ordenado[index])

        valores_comida_temp[posicao_atual] = -1
        indice_comidas_ordenado.append(posicao_atual)

    # ORDENANDO CONVIDADOS - Verificando empate para ordem lexicográfica

    qtd_convidados = len(convidados)
    convidados_ordenados = []
    convidados_empatados = []
    empatou = False

    for comida_convidado in range(qtd_convidados):

        comida_atual = indice_comidas_ordenado[comida_convidado]
        convidado_desordenado = convidados[comida_atual]

        if comida_convidado < qtd_convidados - 1:
            
            comida_posterior = indice_comidas_ordenado[comida_convidado + 1]

            # Checa se o próximo item é de mesmo valor
            if valores_comidas[comida_atual] == valores_comidas[comida_posterior]:
                convidados_empatados.append(convidado_desordenado)
                empatou = True

            # Caso True, o(s) item(s) anteriores eram de mesmo valor, então ordenar lexicograficamente e add na lista
            elif empatou:

                convidados_empatados.append(convidado_desordenado)
                convidados_empatados.sort()

                for convidado in convidados_empatados:
                    convidados_ordenados.append(convidado)

                empatou = False
                convidados_empatados = []

            else:
                convidados_ordenados.append(convidado_desordenado)

        # Ùltima iteração do for
        else:
            if empatou:
                convidados_empatados.append(convidado_desordenado)
                convidados_empatados.sort()

                for convidado in convidados_empatados:
                        convidados_ordenados.append(convidado)
            
            else:
                convidados_ordenados.append(convidado_desordenado)


    # PRINT comidas
    comida_mais_cara = convidados.index(convidados_ordenados[-1])

    print(f"Obrigado para o(a) {convidados_ordenados[-1]} pelo(a) excelente {comidas[comida_mais_cara]}")
    
    if len(convidados) > 1:
        comida_mais_barata = convidados.index(convidados_ordenados[0])

        print(f"Rapaz, {convidados_ordenados[0]} trouxe o(a) {comidas[comida_mais_barata]} que estava altamente mais ou menos!!!")


    # PRINT dos convidados
    print("Lista de convidados do Calabreso")

    for posicao, convidado in zip(range(qtd_convidados), convidados_ordenados):
        print(f"{posicao + 1}- {convidado}")