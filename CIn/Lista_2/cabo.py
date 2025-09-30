print("Começa agora o treinamento para grande final mundial de cabo de guerra!")

qtd_partidas = 0

while qtd_partidas % 2 == 0:
    qtd_partidas = int(input())

    if qtd_partidas % 2 == 0:
        print("Não deverá haver empates! O número de partidas deverá ser ímpar.")
    else:
        print(f"Eles batalharão em {qtd_partidas} longas partidas.")

forca_arthur = int(input())
forca_joao = int(input())

resistencia = int(input())

pontos_arthur = 0
pontos_joao = 0

diff_arthur = 0
diff_joao = 0

partidas_jogadas = 0
diferenca_placar = True

while partidas_jogadas < qtd_partidas and diferenca_placar:

        print(f"Começa a {partidas_jogadas + 1}ª partida!")
        print(f"Placar geral: {pontos_arthur} X {pontos_joao}")

        resistencia_joao = resistencia
        resistencia_arthur = resistencia
        
        while resistencia_joao > 0 and resistencia_arthur > 0:
            rodada = int(input())

            primo = True
            quadrado_perfeito = False

            limite_verificacao = round((rodada**0.5))
            if rodada != 2 and rodada != 3:
                primo = True if rodada % 2 != 0 else False
                
                if primo:
                    for numero in range(3, limite_verificacao + 1, 2):
                        if rodada % numero == 0:
                            primo = False

            if not primo:
                for numero in range(limite_verificacao + 1):
                    if numero**2 == rodada:
                        quadrado_perfeito = True

            if quadrado_perfeito:
                print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
                resistencia_arthur += 1
                resistencia_joao -= 1

            elif primo:
                print("O primo do primo é primo do primo? João puxa mais forte!")
                resistencia_joao += 1
                resistencia_arthur -= 1 

            else:
                if forca_joao > forca_arthur:
                    print("João é o mais forte! Arthur não consegue segurar.")
                    resistencia_joao += 1
                    resistencia_arthur -= 1 

                else:
                    print("Arthur é o mais forte! João não consegue segurar.")
                    resistencia_arthur += 1
                    resistencia_joao -= 1

        if resistencia_arthur > 0:
            pontos_arthur += 1
            print("Arthur dá orgulho para Maceió e ganha a partida!")
        else:
            pontos_joao += 1
            print("João usa seus talentos de mangueboy e leva essa para casa!")


        diff_arthur = pontos_arthur - pontos_joao
        diff_joao = pontos_joao - pontos_arthur
        
        partidas_jogadas += 1
        diferenca_placar = abs(diff_arthur) < (qtd_partidas - partidas_jogadas)

print(f"\nAgora eles estão prontos para o mundial!")
print(f"Placar final: {pontos_arthur} X {pontos_joao}")

ganhador = "Arthur" if pontos_arthur > pontos_joao else "João"

if pontos_arthur == 0:
    print(f"Arthur não teve chance! João venceu todas as partidas.")
elif pontos_joao == 0:
    print(f"João não teve chance! Arthur venceu todas as partidas.")
else:
    if ganhador == "João":
        print(f"O ganhador foi {ganhador} com uma diferença de {diff_joao} partidas.")
    else:
        print(f"O ganhador foi {ganhador} com uma diferença de {diff_arthur} partidas.")