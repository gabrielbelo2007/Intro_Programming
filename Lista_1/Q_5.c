//
// Created by gabrielbelo on 16/05/25.
//

#include <stdio.h>

void main()
{
    printf("Jogador 1 digite os 3 caracteres secretos: ");
    char secreto_1, secreto_2, secreto_3;
    scanf("%c %c %c", &secreto_1, &secreto_2, &secreto_3);
    printf("\n\n\n\n\n\n"); // Esconder letras secretas
    getchar();

    int descoberto_1 = 0, descoberto_2 = 0, descoberto_3 = 0;
    int tentativas = 15, restantes = 3, acertos = 0;

    while (tentativas > 0 && acertos < 3)
    {
        char palpite;
        printf("Tentativa: ");
        scanf("%c", &palpite);
        getchar();

        if (palpite == secreto_1)
        {
            if (descoberto_1 == 0)
            {
                --restantes;
                printf("Você descobriu uma letra secreta restam %i\n", restantes);
                acertos++;
                descoberto_1 = 1;
            }
            else
            {
                printf("Você já descobriu essa letra, escolha uma nova.\n");
            }
        }

        else if (palpite == secreto_2)
        {
            if (descoberto_2 == 0)
            {
                --restantes;
                printf("Você descobriu uma letra secreta restam %i\n", restantes);
                acertos++;
                descoberto_2 = 1;
            }
            else
            {
                printf("Você já descobriu essa letra, escolha uma nova.\n");
            }
        }

        else if (palpite == secreto_3)
        {
            if (descoberto_3 == 0)
            {
                --restantes;
                printf("Você descobriu uma letra secreta restam %i\n", restantes);
                acertos++;
                descoberto_3 = 1;
            }
            else
            {
                printf("Você já descobriu essa letra, escolha uma nova.\n");
            }
        }

        else
        {
            tentativas--;
            printf("Você errou restam %i letras e %i tentativa(s)\n", restantes, tentativas);
        }
    }
    if (acertos == 3)
    {
        printf("Parabéns você descobriu todas as letras!");
    }
    else
    {
        printf("Você não conseguiu acertar todas, pontuação total: %i", acertos);
    }
}