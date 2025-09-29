print("Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?")

participantes = int(input())

palavras = ""

nome_inicial = input()
palavra_referencia = input()

palavras_diferentes = 0
palavra_atual = palavra_referencia
nome1 = ''
nome2 = ''

for participante in range(participantes - 1):
    nome_participante = input()
    palavra_escutada = input()

    if palavra_escutada != palavra_atual:
        palavra_atual = palavra_escutada

        palavras_diferentes += 1
        print(f"Parece que {nome_participante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…")

        if palavras_diferentes == 1:
            nome1 = nome_participante
            palavra_errada = palavra_escutada

        nome2 = nome_participante if palavras_diferentes == 2 else nome2

        if palavras_diferentes == 5:
            print(f"Caramba, que confusão! A palavra {palavra_referencia} já tá toda embaralhada e virou {palavra_escutada}!")

if palavras_diferentes == 0:
    print(f"Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {palavra_referencia}! Talvez os telefones modernos comecem a perder espaço pra moda antiga.")

elif palavras_diferentes > 0 and palavra_escutada == palavra_referencia:
    print(f"Parece que ocorreram {palavras_diferentes} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {palavra_referencia} conseguiu chegar no fim do telefone sem fio.")

else:
    if palavras_diferentes == 1:
        print(f"Poxa, foi por pouco, só quem errou foi {nome1} que disse {palavra_escutada} ao invés de {palavra_referencia}…")
    elif palavras_diferentes == 2:
        print(f"Se não fosse pelos erros de {nome1} e {nome2} a palavra {palavra_referencia} poderia ter chegado até o fim, talvez eles devessem tentar de novo.")
    else:
        print(f"É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {palavra_referencia} acabou virando {palavra_escutada}. No total, ocorreram {palavras_diferentes} trocas.")