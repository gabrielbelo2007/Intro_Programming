def modificao_codigo(hora_morte, hora_modificao):
    
    if hora_modificao > hora_morte:
        return True
    
    return False

def digitais_elisson_joao(digitais):
    presentes = []

    for digital in digitais:

        if digital == "Elisson":
            presentes.append("Elisson")
        
        if digital == "João Guilherme":
            presentes.append("João Guilherme")
    
    return presentes


print("TRIBUNAL EM SESSÃO")
print(f"Juiz: Que comece o julgamento do caso em pauta.\n")

print("Promotor Edgeworth: A promotoria está pronta, Meritíssimo.")
print(f"Phoenix Wright: (Lá vamos nós... A reputação do escritório está em jogo.) A defesa está pronta.\n")

print("--- SALA DE VISITAS DO TRIBUNAL ---")
print("João Guilherme: Sr. Wright, eu juro, eu não o matei! Eu estive lá, mas... é só isso!")
print(f"Phoenix Wright: (Eu sinto que ele está escondendo algo... Devo pressioná-lo por mais detalhes ou confiar no que ele me disse?)\n")

escolha_inicial = input()

print("--- DE VOLTA AO TRIBUNAL ---")
print("Juiz: Promotoria, apresente as evidências.")
print("Promotor Edgeworth: A promotoria acusa este homem pelo crime de assassinato...")
print("Promotor Edgeworth: ...João Guilherme!")
print("Promotor Edgeworth: Comecemos com a evidência virtual chave, o registro da última modificação no computador da vítima.")

hora_modificao = int(input())

print("Promotor Edgeworth: E, de acordo com o legista, a hora exata da morte.")

hora_morte = int(input())

print("Promotor Edgeworth: Finalmente, a prova irrefutável. O relatório de digitais da arma do crime, o troféu.")

numero_digitais = int(input())

print(f"Promotor Edgeworth: Que o escrivão leia os nomes encontrados na arma...\n")

digitais = []

for digital in range(numero_digitais):
    nome_digital = input()
    digitais.append(nome_digital)

confessou = False

print(f"ARGUMENTOS FINAIS\n")

if escolha_inicial == "pressionar":

    print("--- FLASHBACK: SALA DE VISITAS ---")
    print("Phoenix Wright: HOLD IT! João, não é só isso! Eu não posso te defender se você não me contar tudo. O que realmente aconteceu naquela noite?")
    print("João Guilherme: (soluço)... Certo... Eu vou contar. Não era sobre a rixa... era sobre o 'Ticket Fantasma'.")
    print("João Guilherme: Um bug impossível no sistema da faculdade. Eu criei um código que o resolvia. Era a minha chance de conseguir o estágio dos sonhos.")
    print("João Guilherme: Eu... eu confiei em Arthur. Mostrei o código a ele para uma revisão. E ele... ele o roubou. Apresentou como se fosse dele, levou todo o crédito.")
    print("João Guilherme: E o pior, Sr. Wright... eu cometi o erro de comentar sobre meu progresso com o Elisson, o 'monitor do povo'. Ele era o único, além de mim e de Arthur, que sabia da história toda. Ele observava nossa agilidade com os tickets com um sentimento sombrio! Se houver dedo dele nisso, ele certamente tentará depôr para contar do roubo do meu código por Arthur para me incriminar!")
    print(f"--- FIM DO FLASHBACK ---\n")

    print("Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, suas digitais estão na arma, e a perícia mostra que o arquivo do 'Ticket Fantasma' foi modificado após a morte, provando que ele permaneceu na cena do crime!")
    print(f"Phoenix Wright: OBJEÇÃO!\n")

    if modificao_codigo(hora_morte, hora_modificao) == True:

        print("Phoenix Wright: A sua lógica tem uma falha fatal, promotor! É impossível que meu cliente tenha modificado aquele arquivo!")
        print("Phoenix Wright: Pois a defesa pode provar que, no exato momento da modificação, João Guilherme estava a quilômetros de distância, comprando um café na 'Cafeteria Byte'! Temos o registro da transação e uma testemunha ocular!")
        print("Phoenix Wright: A contradição temporal, combinada com este álibi, prova apenas uma coisa: a existência de uma terceira pessoa na cena do crime!")

        if "Elisson" in digitais_elisson_joao(digitais):

            print("Phoenix Wright: Se meu cliente tem um álibi, quem poderia ser? Quem alteraria o arquivo do 'Ticket Fantasma' para incriminar João Guilherme?")
            print("Phoenix Wright: Só poderia ser alguém que conhecia a história... alguém que meu cliente confessou ter contado!")
            print("Phoenix Wright: A defesa descobriu que apenas UMA outra pessoa sabia da história do código... uma pessoa cujas digitais, convenientemente, também estão na arma do crime!")
            print("Phoenix Wright: A pessoa que matou Arthur Sean para eliminar um rival e incriminar o outro foi você...")
            print(f"Phoenix Wright: ELISSON!!!\n")

            print("Elisson: N-NÃÃÃÃÃOOOOO! COMO... ELE TE CONTOU?! MEU PLANO ERA PERFEITO!")
            confessou =  True
        
        print()
        veredito = "INOCENTE"

    elif "João Guilherme" not in digitais_elisson_joao(digitais):

        print(f"Phoenix Wright: A promotoria não pode sequer provar que meu cliente tocou na arma do crime! Não há digitais dele!\n")
        veredito = "INOCENTE"

    else:

        print(f"Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Não tenho objeções...)\n")
        veredito = "CULPADO"

else:

    print(f"(Voz da Consciência de Phoenix: Eu confiei em João... mas agora, essa 'hora da modificação' não faz sentido para mim. Não tenho como usar essa evidência!)\n")

    print("Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, e suas digitais estão na arma. O caso está encerrado.")
    print(f"Phoenix Wright: OBJEÇÃO!\n")

    if "João Guilherme" not in digitais_elisson_joao(digitais):

        print(f"Phoenix Wright: A promotoria não pode provar que meu cliente tocou na arma do crime! Não há digitais dele!\n")
        veredito = "INOCENTE"

    else:

        print(f"Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Estou sem argumentos!)\n")
        veredito = "CULPADO"


print("Juiz: ...Compreendo. Após analisar todas as evidências e os argumentos...")
print(f"Juiz: O veredito para o caso de João Guilherme é: {veredito}!\n")

if veredito == "INOCENTE":

    if confessou:
        print("Juiz: Que esta corte jamais esqueça o dia em que a verdade foi revelada contra todas as probabilidades.")
    
    print("A reputação do escritório Fey & Co. continua impecável.")

else:

    print("Edgeworth... Você ainda não venceu o debate final.")