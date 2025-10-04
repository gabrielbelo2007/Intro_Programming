art_sheldon = int(input())
art_leonard = int(input())
art_raj = int(input())
art_howard = int(input())

exp_sheldon = int(input())
exp_leonard = int(input())
exp_raj = int(input())
exp_howard = int(input())

pts_sheldon = art_sheldon * 2 + exp_sheldon * 3
pts_leonard = art_leonard * 2 + exp_leonard * 3
pts_raj = art_raj * 2 + exp_raj * 3
pts_howard = art_howard * 2 + exp_howard * 3

print(f"Pontuação final:")
print(f"Sheldon: {pts_sheldon}")
print(f"Leonard: {pts_leonard}")
print(f"Raj: {pts_raj}")
print(f"Howard: {pts_howard}")

pts_empatado = max(pts_sheldon, pts_raj, pts_howard, pts_leonard)
if((pts_sheldon > pts_leonard and pts_sheldon > pts_raj and pts_sheldon > pts_howard) or pts_empatado == pts_sheldon):
    ganhador = "Sheldon"
elif((pts_leonard > pts_howard and pts_leonard > pts_raj) or pts_empatado == pts_leonard):
    ganhador =  "Leonard"
elif((pts_raj > pts_howard) or pts_empatado == pts_raj):
    ganhador = "Raj"
else:
    ganhador = "Howard"

print(f"\nO cientista da semana é: {ganhador}")

if(ganhador == "Sheldon"):
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif(ganhador == "Leonard"):
    print("A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
elif(ganhador == "Raj"):
    print("Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
else:
    print("Um pequeno passo para a ciência, um grande salto para alguém com mestrado.")