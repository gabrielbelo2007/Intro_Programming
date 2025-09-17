nome_item = input().lower()
valor_item = round(float(input()))
responsavel = input().lower()
evento = input().lower()

# 0 - REPROVADO | 1 - APROVADO | 2 - APROVADO COM RESSALVAS

aprovado = 1
if(responsavel == "angela"):
    if(valor_item > 100):
        texto = "Apenas eu tenho discernimento para gastos desta magnitude."
    else:
        texto = "Compra feita por mim, obviamente dentro dos padrões de excelência."

elif(valor_item > 100):
    texto = "Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!"
    aprovado = 0

elif(responsavel == "michael"):
    if(nome_item == "mágica" or nome_item == "fantasia"):
        texto = "O Comitê não financia frivolidades e palhaçadas, Michael."
        aprovado = 0
    elif(valor_item > 60):
        aprovado = 2
        if(evento == "natal"):
            texto = "O espírito natalino de Michael é... excessivo. A nota será conferida."
        elif(evento == "aniversário"):
            texto = "Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!"
    else:
        texto = "Uma compra surpreendentemente sensata vinda do Michael. Suspeito."

elif(evento == "halloween"):
    aprovado = 2
    if(nome_item == "abóbora"):
        if(valor_item <= 30):
            aprovado = 1
            texto = "Uma abóbora de tamanho e custo razoáveis. Eficiente."
        else:
            texto = "Por que uma abóbora precisa ser tão cara? Extravagância."
    else:
        texto = "Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo."

elif(evento == "aniversário"):
    aprovado = 1
    if(nome_item == "sorvete de menta com chocolate"):
        aprovado = 0
        texto = "Este sabor de sorvete é uma abominação e não entrará em meu evento."
    else:
        if(nome_item == "bolo" and valor_item <= 40):
            texto = "Um bolo modesto para celebrar mais um ano de produtividade, parabéns!"
        else:
            texto = "Itens de aniversário devem ser práticos, não uma distração do trabalho."

elif(valor_item > 50):
    aprovado = 2
    texto = "Está dentro do orçamento, mas não quer dizer que não vou verificar!"

else:
    texto = "Esta compra não viola nenhum regulamento... por enquanto."

if(aprovado == 0):
    print("Compra Reprovada!")
elif(aprovado == 1):
    print("Compra Aprovada!")
else:
    print("Compra Aprovada com ressalvas!")

print(texto)