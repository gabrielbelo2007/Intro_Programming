exigencias_ariana = {}

# FASE 1
exigencia = ""
while exigencia != "MIMOS RECEBIDOS":
    exigencia = input()

    if exigencia != "MIMOS RECEBIDOS":
        categoria, item_pricipal, qtd_item = exigencia.split(": ")

        if item_pricipal == "latte":
            qtd_item = int(qtd_item)
            qtd_item += 1

        exigencias_ariana.update({categoria:(item_pricipal, int(qtd_item))})

# FASE 2
reabastecimento = ""
while reabastecimento != "ACABOU, a Glinda está pronta!":
    reabastecimento = input()

    if reabastecimento != "ACABOU, a Glinda está pronta!":
        dados = reabastecimento.split(" ")
        
        quantidade_recebida = int(dados[1])
        categoria_recebida = dados[5]
        item = dados[7][:-1] # Eliminar o parêntese do final

        valor_categoria = exigencias_ariana.get(categoria_recebida, "")

        if valor_categoria != "":
            nova_quantidade = valor_categoria[1] - quantidade_recebida
            exigencias_ariana.update({categoria_recebida:(item, nova_quantidade)})

# RELATORIO
print("Relatório de Balanço Final:")
estoque_negativo = 0

gloss, latte = False, False # CHECAGEM ESPECIAL

for categoria in exigencias_ariana.keys():
    item_pricipal, qtd_item = exigencias_ariana[categoria]

    if qtd_item <= 0:
        status = "Você entregou TUDO! O mimo tá mais que garantido."

        if item_pricipal == "Gloss":
            gloss = True
        
        elif item_pricipal == "latte":
            latte = True

    else:
        status = f"Golpe BAIXÍSSIMO! Faltam {qtd_item} mimos. Corre!"
        estoque_negativo += 1
    
    print(f"Categoria: {categoria} Item: {item_pricipal} Status: {status}")


print()
if gloss:
    print("TUDO! O Gloss tá on. O look de Glinda tá salvo!")
else:
    print("CADÊ meu gloss? Como divarei? ... A Glinda tá chorando de raiva!")

if latte:
    print("Latte gelado pronto! A voz de Glinda está salva. Pode vir o próximo take")
else:
    print("Cadeia neles! Faltou o Mimo Sagrado. Essa equipe tá perdida!")

# VEREDITO FINAL

print(f"\nVeredito Final")

if estoque_negativo >= 3:
    print("Thank U, Next! A equipe de camarim foi demitida!")
else:
    print("Estoque Aprovado! Glinda vai brilhar em Wicked!")