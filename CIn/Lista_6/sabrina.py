print("Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?")
print(f"A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…\n")

catalogo_phil = {}

num_casas = int(input())

chaves_desc_casas = ["bairro", "quartos", "preco"]

# Estruturando o dicionário com as casas
for casa in range(num_casas):
    desc_casa = input().split("-")
    
    valores_desc_casa = []
    endereco = desc_casa[1].strip()

    for index_caracteristica in range(len(desc_casa)):
        caracteristica = desc_casa[index_caracteristica].strip()
        
        if index_caracteristica != 1:
            valores_desc_casa.append(caracteristica)

    dict_desc = dict(zip(chaves_desc_casas, valores_desc_casa))
    catalogo_phil.update({endereco: dict_desc})

print(f"Catálogo concluído! Quem será que irá comprar uma casa de Phil?\n")

# Loop de atendimento
nome_cliente = ""
casas_vendidas = 0

while nome_cliente != "FIM":
    nome_cliente = input()

    if nome_cliente != "FIM":
        requisitos = tuple(input().split("-"))

        casas_validas = {}

        casa_valida = False
        for endereco in catalogo_phil:

            for descricao, conteudo in catalogo_phil[endereco].items():

                if descricao == "quartos":
                    if int(conteudo) >= int(requisitos[0]):
                        casa_valida = True
                        score_total = int(conteudo) * 10
                
                elif descricao == "preco":
                    if int(conteudo) > int(requisitos[1]):
                        casa_valida = False

            if casa_valida:
                casas_validas.update({endereco:score_total})
            
        if len(casas_validas) > 0:
            endereco_melhor_score = max(casas_validas, key=casas_validas.get)
            bairro = catalogo_phil[endereco_melhor_score]["bairro"]
            melhor_score = casas_validas[endereco_melhor_score]

            print(f"🎤 Bem-vindo ao House Tour de {bairro}, {nome_cliente}!")
            print(f"➡ Casa: {endereco_melhor_score}")
            print(f"💖 Score: {melhor_score} pontos\n")

            if melhor_score >= 40:
                
                if nome_cliente == "Sabrina Carpenter":
                    print(f'"Uau, Phil! Acho que finalmente encontrei o cenário perfeito para o clipe de House Tour!"\n')

                elif nome_cliente == "Taylor Swift":
                    print(f'"Essa casa é perfeita para passar as férias na praia!"\n')

                else:
                    print(f'"{nome_cliente} ficou encantado(a)! Phil comemora mais uma venda de sucesso!"\n')

                print(f'Venda concluída! Phil dança triunfante ao som de "House Tour"!\n')
                casas_vendidas += 1
                
            else:

                if nome_cliente == "Sabrina Carpenter":
                    print(f'"Hmm... Sabe Phil, a letra não era tão literal assim…"\n')

                elif nome_cliente == "Taylor Swift":
                    print(f'"Nós nunca vamos comprar essa casa juntos, Phil!"\n')
                
                else:
                    print(f'"Parece que a música não ajudou nas vendas dessa vez…"\n')

                print(f"Talvez a Sabrina realmente não estivesse falando de imóveis…\n")

        else:
            print(f"Puxa, {nome_cliente}, vou te avisar se algo aparecer. Não tenho nada com esses requisitos.\n")

print("===== RELATÓRIO DE VENDAS =====")
print(f"Total de casas vendidas: {casas_vendidas}")
print("===============================")