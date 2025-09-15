nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

qtd_aulas = int(input())
qtd_faltas = int(input())

media = (nota1 + nota2 + nota3) / 3
presenca = 100 - (qtd_faltas / qtd_aulas) * 100

print(f"Chris, você conseguiu média {media:.2f} e {presenca:.2f}% de presença.")

if(presenca >= 75):
    if(media >= 8):
        print("Chris está APROVADO por nota e por presença!🎉")
        print("Pisante maneiro, Chris! Agora é só torcer pros outros não vacilarem.")
    elif(media >= 7):
        print("Chris está APROVADO!✅")
        print("Sacomé, né? Passou raspando, mas a pizza ainda ficou longe.")
    else:
        print("Chris ESTÁ REPROVADO por NOTA.❌")
        print("Chris, já pro seu quarto ou eu vou te bater até você virar o avesso!")
else:
    if(media >= 7):
        print("Chris ESTÁ REPROVADO por FALTA.❌")
        print("Trágico! Não adianta só saber, tem que aparecer.")
    else:
        print("Chris ESTÁ REPROVADO por NOTA e por FALTA.❌")
        print("Chris, você perdeu o juízo? Eu trouxe você para esse mundo e posso muito bem tirar você dele.")