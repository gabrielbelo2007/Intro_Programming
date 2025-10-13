num_convidados = input()

convidados = []
comidas = []
valores_comidas = []
comida_mais_cara = 0
comida_mais_barata = 0

for convidado in range(num_convidados):
    nome_convidado = input()
    comida_convidado = input()
    valor_comida = input()
    
    if nome_convidado == "Maicon Kuster":
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    
    elif comida_convidado in comidas:
        print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {nome_convidado}")
    
    else:
        convidados.append(nome_convidado)
        comidas.append(comida_convidado)
        valores_comidas.append(valor_comida)
    
        if valor_comida > comida_mais_cara:
            index_comida_cara = (comidas.count() - 1)
        
        elif valor_comida < comida_mais_barata:
            index_comida_barata = (comidas.count() - 1)

if convidados.count() == 0:
    print("Nenhum convidado marcou presença na festa do calabreso!")

else:
    print(f"Obrigado para o(a) {convidados[index_comida_cara]} pelo(a) excelente {comidas[index_comida_cara]}")
    
    if convidados.count() > 1:
        print(f"Rapaz, {convidados[index_comida_barata]} trouxe o(a) {comidas[index_comida_barata]} que estava altamente mais ou menos!!!")
    
    contador = 0
    valores_analiados = []
    for comidas in range(comidas):
        menor_valor = 0
        for index in valores_comidas:
            if valores_comidas[index] < menor_valor:
                menor_valor = valores_comidas[index]
        
        contador += 1
       # print(f"{contador}- {}")