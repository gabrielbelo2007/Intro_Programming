casos = int(input())
dias = int(input())
assis_casos = int(input())
op_campos = int(input())
op_especial = input()

if(op_especial == "sim"):
    tipo_op_especial = input()

localizacao = input()

# 0 -> Desclassificado | 1 -> Classificado

classificado = True
if(classificado):
    if(localizacao != "Manhattan" and localizacao != "Brooklyn"):
        print("Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!")
        classificado = False
    else:
        print("Pelo menos nos bairros corretos Jake está!")

if(classificado):
    if(casos >= 20):
        print("Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.")
    else:
        classificado = False
        print("Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")

if(classificado):
    if(casos / dias >= 0.5):
        print("Parece que Jake é bem consistente na sua média diária de casos.")
    else:
        classificado = False
        print("A média diária de casos tá muito baixa, Peralta foi desclassificado.")

if(classificado):
    if(assis_casos >= 5):
        print("Peralta ajudou bastante outros detetives, ele ainda está na competição!")
    else:
        classificado = False
        print("Desclassificado! Jake precisa ajudar mais os companheiros.")

if(classificado):
    if(op_campos >= 20):
        print("Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?")
    else:
        classificado = False
        print("Peralta precisa sair mais da delegacia, está faltando ação em campo!")

if(classificado):
    if(op_especial == "sim"):
        print("Minha nossa! Jake Peralta é realmente um detetive diferenciado.")
    else:
        print("Para que operação especial quando se tem números, não é?")

if(classificado):
    pontuacao = (casos * 2) + (assis_casos * 1.5) + (op_campos * 0.5)
    if(op_especial == "sim"):
        if(tipo_op_especial == "Infiltração"):
            pontuacao += pontuacao * 0.5
        elif(tipo_op_especial == "Escuta"):
            pontuacao += pontuacao * 0.3
        elif(tipo_op_especial == "Invasão"):
            pontuacao += pontuacao * 0.2
        else:
            pontuacao += pontuacao * 0.1

    if(pontuacao >= 70):
        print("Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?")
    elif(40 <= pontuacao < 70):
        print("Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.")
    else:
        print("Muito difícil de Jake ganhar o prêmio.")