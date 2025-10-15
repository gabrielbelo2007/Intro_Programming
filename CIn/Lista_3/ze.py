numero_eventos = int(input())

regra_1 = False
eventos = []
for evento in range(numero_eventos):
    dados_evento = input()

    if "VJM" in dados_evento:
        regra_1 = True
    
    if not regra_1:
        eventos.append(dados_evento.split(" - "))

print(f"Iniciando investigação... Zé Felipe está focado.")

nivel_suspeita = 0

if not regra_1:

    # Ordenar os eventos
    trocou = True
    verificados = 0
    while trocou and verificados <  len(eventos) - 1:
        trocou = False
        
        for evento in range(0, len(eventos) - 1):
            if(eventos[evento][2] > eventos[evento + 1][2]) or (eventos[evento][2] == eventos[evento + 1][2] and eventos[evento][3] > eventos[evento + 1][3]):
                eventos[evento], eventos[evento + 1] = eventos[evento + 1], eventos[evento]
                trocou = True

        verificados += 1

    encontros_suspeitos = 0
    alibis = 0

    for evento_virginia in eventos:
        if evento_virginia[0] == "V":

            local_v = evento_virginia[1]
            horario_inicio_v = evento_virginia[2]
            horario_final_v = evento_virginia[3]

            for evento_suspeito in eventos:

                suspeito = evento_suspeito[0]
                local_suspeito = evento_suspeito[1]
                horario_inicio_s = evento_suspeito[2]
                horario_final_s = evento_suspeito[3]

                if (horario_inicio_s < horario_final_v and horario_inicio_v < horario_final_s) or (horario_inicio_v < horario_final_s and horario_inicio_s < horario_final_v):

                    if suspeito == "JM" and local_suspeito == local_v:
                        nivel_suspeita += 35
                        encontros_suspeitos += 1
                    
                    elif suspeito == "ZF" and local_suspeito == local_v:
                        nivel_suspeita -= 20 if nivel_suspeita - 20 >= 0 else nivel_suspeita
                        alibis += 1

    print()               
    print("--- Linha do Tempo dos Eventos ---")

    for evento in eventos:

        nome = "Virgínia" if evento[0] == "V" else "Jogador Misterioso" if evento[0] == "JM" else "Zé Felipe"
        print(f"{evento[2]}-{evento[3]}: {nome} - {evento[1]}")

    print()
    print("--- Resumo da Análise ---")
    print(f"Encontros Suspeitos: {encontros_suspeitos}")
    print(f"Álibis Confirmados: {alibis}")

print()
if regra_1 or nivel_suspeita >= 100:
    print("TRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.")

elif nivel_suspeita >= 70 and nivel_suspeita <= 99:
    print(f"Nível de Suspeita: {nivel_suspeita} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia.")

elif nivel_suspeita >= 30 and nivel_suspeita <= 69:
    print(f"Nível de Suspeita: {nivel_suspeita} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho.")

else:
    print(f"Nível de Suspeita: {nivel_suspeita} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor.")