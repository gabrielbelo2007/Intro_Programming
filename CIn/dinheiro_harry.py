# Questão - Monitoria IP

G = int(input())
S = int(input()) 
K = int(input())

qtd_itens = int(input())
itens = []

for item in range(qtd_itens):

    novo_item = input().split(", ")
    itens.append(novo_item)

tabela_npm = [[] for _ in range(K + 1)]
tabela_npm[0] = [0]

"""
A ideia é que essa tabela NPM comece do 0 até o valor de K.

Onde cada índice representa o valor de NPM, e cada sublista armazena o valor necessário para alcançar aquele NPM.

Por isso que o índice 0 recebe 0 assim que a tabela é inicializada, pois para chegar em 0 de NPM não é necessário nenhum item.

Após isso, para cada item, é registrado o quanto ele fornece de NPM e o custo, aproveitando dos custos já registrados dos itens anteriores.

Por isso, que cada coluna que representa um valor de NPM é uma lista, armazenando todos os custos possíveis que resultam nesse valor de NPM.
"""

for item in itens:

    custo_item, npm_item = int(item[0]),int(item[1])

    for i in range(K + 1):

        for custo_existente in tabela_npm[i]:
            novo_npm = i + npm_item

            if novo_npm > K:
                novo_npm = K
            
            novo_custo = custo_existente + custo_item
            
            if novo_custo <= G:
                
                # Evitar salvar resultados que dão o NPM pelo mesmo valor
                existe = False
                for custo_registrado in tabela_npm[novo_npm]:
                    
                    if custo_registrado == novo_custo:
                        existe = True
                        
                if not existe:
                    tabela_npm[novo_npm].append(novo_custo)

# Todos os valores que atingiram no mínimo o valor K de NPM
custos_que_atingem_npm = tabela_npm[K]

if len(custos_que_atingem_npm) == 0:
    print("Harry não atingiu o preparo necessário.")

else:
    # Filtrar custos que permitem a reserva S
    custos_validos = []

    for custo in custos_que_atingem_npm:
        if (G - custo) >= S:
            custos_validos.append(custo)
    
    if len(custos_validos) == 0:
        print("Vou ter que levar só alguns chocolates mesmo!")

    else:
        custos_validos.sort(reverse=True)

        for v in custos_validos:
            print(f"Custo encontrado: {v}")

        print(f"O menor gasto possível para Harry será: {custos_validos[-1]} Galeões!")
        print("Rony e Hermione ficarão muito feliz!")