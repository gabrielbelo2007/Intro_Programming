valores_comidas = [40, 20, 30]

trocou = True
valores_comidas_ordenado = []
qtd_comida = len(valores_comidas)

while trocou:
    trocou = False

    for index in range(0, qtd_comida - 1):
        if (valores_comidas[index] < valores_comidas[index + 1]) and index not in valores_comidas_ordenado:
            maior_valor = index + 1
            trocou = True

    if trocou:
        valores_comidas_ordenado.append(maior_valor)

print(valores_comidas_ordenado)