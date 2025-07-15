#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

typedef struct
{
    char nome[100];
    float defesa;
    float ataque;
    float vida;

}Lutador;

void inicializar_time(Lutador jogador[], int tam, int time)
{

    printf("Defina o nome dos lutadores do time %i\n\n", time);
    for (int i = 0; i < tam;)
    {
        printf("Digite o nome do lutador %i: ", i+1);
        scanf("%s", jogador[i].nome);
        getchar();

        if (i > 0)
        {
            if (strcmp(jogador[i].nome, jogador[i-1].nome) == 0)
            {
                printf("\nDigite um nome único para cada lutador!\n\n");
            }
            else
            {
                jogador[i].defesa = (rand() % 11);
                jogador[i].ataque = (rand() % 11);
                jogador[i].vida = 100;
                i++;
            }
        }
        else
        {
            jogador[i].defesa = (rand() % 11);
            jogador[i].ataque = (rand() % 11);
            jogador[i].vida = 100;
            i++;
        }
    }
    printf("\n\n");
}

void imprimir_status(Lutador jogador[], int tam)
{
    for (int  i = 0; i < tam; i++)
    {
        printf("%s\n", jogador[i].nome);
        printf("%.2f\n", jogador[i].defesa);
        printf("%.2f\n", jogador[i].ataque);
        printf("%.2f\n\n", jogador[i].vida);
    }

}

float calcular_precisao(Lutador jogador_atacante)
{

}

float atacar(Lutador jogador_atacante, Lutador jogador_defensor)
{

}

void atualizar_vida(float ataque, Lutador jogador_defensor)
{

}

void jogar()
{
    srand(time(NULL));

    Lutador jogador1[4];
    Lutador jogador2[4];

    inicializar_time(jogador1, 4, 1);
    inicializar_time(jogador2, 4, 2);

    imprimir_status(jogador1, 4);
    imprimir_status(jogador2, 4);

    int vida_jogador1 = 400;
    int vida_jogador2 = 400;

    do
    {
        int time_inicial = (rand() % 2) + 1;

        if (time_inicial == 1)
        {

        }
        else
        {

        }
    }while (vida_jogador1 > 0 && vida_jogador2 > 0);
}

void main()
{
    jogar();
}