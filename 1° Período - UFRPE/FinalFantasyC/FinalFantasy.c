#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

typedef struct
{
    int id;
    char nome[100];
    float defesa;
    float ataque;
    float vida;
    int ativo;

}Jogador;

int equipe = 1; // Numerar os times na inicialização e impressão inicial
void inicializar_time(Jogador lutador[], int tam)
{
    printf("Defina o nome dos lutadores do time %i\n\n", equipe);
    for (int i = 0; i < tam;)
    {
        lutador[i].id = i+1; // ID começa em 1 para ficar mais visual ao usuário

        printf("Digite o nome do lutador %i: ", i+1);
        scanf("%s", lutador[i].nome);
        getchar();

        // Verifica se os lutadores têm nomes iguais
        if (i > 0)
        {
            if (strcmp(lutador[i].nome, lutador[i-1].nome) == 0)
            {
                printf("\nDigite um nome único para cada lutador!\n\n");
            }
            else
            {
                lutador[i].defesa = (rand() % 10) + 1;
                lutador[i].ataque = (rand() % 10) + 1;
                lutador[i].vida = 100;
                lutador[i].ativo = 1;
                i++;
            }
        }
        else
        {
            lutador[i].defesa = (rand() % 10) + 1;
            lutador[i].ataque = (rand() % 10) + 1;
            lutador[i].vida = 100;
            lutador[i].ativo = 1;
            i++;
        }
    }
    printf("\n");
}

void imprimir_equipe(Jogador lutador[], int tam)
{
    printf("Equipe %i:\n\n", equipe);
    for (int  i = 0; i < tam; i++)
    {
        printf("Nome: %s\n", lutador[i].nome);
        printf("Vida: %.2f\n", lutador[i].vida);
        printf("Ataque: %.2f\n", lutador[i].ataque);
        printf("Defesa: %.2f\n\n", lutador[i].defesa);

    }
    equipe++;
}

void imprimir_lutador(Jogador lutador[], int selecionado)
{
    printf("ID: %i\n", lutador[selecionado].id);
    printf("Nome: %s\n", lutador[selecionado].nome);
    printf("Vida: %.2f\n", lutador[selecionado].vida);
    printf("Ataque: %.2f\n", lutador[selecionado].ataque);
    printf("Defesa: %.2f\n\n", lutador[selecionado].defesa);
}

int escolha_ataque(Jogador lutador[], int tam)
{
    int escolhido;
    for (int  i = 0; i < tam; i++)
    {
        printf("ID: %i\n", lutador[i].id);
        printf("Nome: %s\n", lutador[i].nome);
        printf("Vida: %.2f\n\n", lutador[i].vida);
    }
    printf("Digite o ID do lutador que você quer atacar: ");
    int verificar_scanf = scanf("%i", &escolhido);
    getchar();

    while (escolhido < 1 || escolhido > 4 || verificar_scanf == 0)
    {
        printf("Digite um ID válido!\n");
        printf("Digite o ID do lutador que você quer atacar: ");
        verificar_scanf = scanf("%i", &escolhido);
        getchar();
    }

    escolhido--; // Ajustar para ficar como índice que começa em 0
    return escolhido;
}

float atacar(float lutador_ataque, float lutador_vida)
{
    float acerto = rand() % 2;
    float precisao = 1 - (lutador_ataque *  lutador_vida)/1000;

    if (precisao >= acerto)
    {
        return lutador_ataque;
    }
    return 0;
}

float defender_contra_atacar(Jogador jogador_defensor[], int escolha, int atacado)
{
    switch (escolha)
    {
    case 0:
        float consegue_defender = rand() % 51;
        float defendeu = (jogador_defensor[atacado].defesa * (consegue_defender/100)) * -1;
        defendeu = (defendeu == 0) ? -1 : defendeu;
        return defendeu;

    case 1:
        int consegue_contra_atacar = rand() % 2;
        if (consegue_contra_atacar == 0)
        {
            jogador_defensor[atacado].ativo = 0;
            return 0;
        }
        return jogador_defensor[atacado].ataque;
    }
}

float escolher_defender_contra_atacar(float vida_lutador_atacante, Jogador jogador_defensor[], int atacado, int numero_time)
{
    printf("\n\n\n\n\nO jogador %i vai receber um ataque!\n", numero_time);
    printf("====================\n");

    imprimir_lutador(jogador_defensor, atacado);

    // Informa só a vida para o único parametro a ser analisado pelo defensor ser a precisão
    printf("Um lutador com %.2f de vida está com você na mira!\n", vida_lutador_atacante);
    printf("Você quer Defender(0) ou Contra-atacar(1): ");

    int acao;
    int verificar_scanf = scanf("%i", &acao);
    getchar();

    while (acao != 0 && acao != 1 || verificar_scanf == 0)
    {
        printf("Digite uma ação válida! Defender(0) ou Contra-atacar(1): ");
        verificar_scanf = scanf("%i", &acao);
        getchar();
    }

    return defender_contra_atacar(jogador_defensor, acao, atacado);
}


float vida_jogador1 = 400;
float vida_jogador2 = 400;
void atualizar_vida(Jogador jogador[], int selecionado, float dano, int numero_jogador)
{
    jogador[selecionado].vida -= dano;
    if (numero_jogador == 1)
    {
        vida_jogador1 -= dano;
    }
    else
    {
        vida_jogador2 -= dano;
    }
}

void ataque(Jogador jogador_atacante[], Jogador jogador_defensor[], int tam, int numero_jogador)
{
    for (int atacante = 0; atacante < tam;)
    {
        printf("\n\n\n\n\nO jogador %i está atacando!\n", numero_jogador);
        printf("====================\n");
        if (jogador_atacante[atacante].ativo == 1 && jogador_atacante[atacante].vida > 0)
        {
            imprimir_lutador(jogador_atacante, atacante);
            float dano = atacar(jogador_atacante[atacante].ataque, jogador_atacante[atacante].vida);
            int atacado = escolha_ataque(jogador_defensor, tam);

            int numero_jogador_defensor = (numero_jogador == 2) ? numero_jogador -1 : numero_jogador + 1;

            float acao_defensor = escolher_defender_contra_atacar(jogador_atacante[atacante].vida, jogador_defensor, atacado, numero_jogador_defensor);

            if (acao_defensor == 0)
            {
                printf("O lutador %s do jogador %i errou o contra-ataque e não vai poder atacar no próximo turno!", jogador_defensor[atacado].nome, numero_jogador_defensor);
            }
            else if (acao_defensor > 0) // Defensor contra_atacou
            {
                printf("O lutador %s do jogador %i acertou o contra-ataque e deu %.2f de dano sem receber dano!", jogador_defensor[atacado].nome, numero_jogador_defensor, jogador_defensor[atacado].ataque);
                atualizar_vida(jogador_atacante, atacante, acao_defensor, numero_jogador);
            }
            else // Defensor defendeu
            {
                if (dano == 0)
                {
                    printf("O lutador %s do jogador %i errou o ataque!", jogador_atacante[atacante].nome, numero_jogador);
                }
                else
                {
                    dano += acao_defensor;
                    if (dano < 0)
                    {
                        // Caso o defensor tenha defendido tudo, o valor da defesa será igual ao dano, apenas para melhor visual
                        acao_defensor = dano;
                        dano = 0;
                    }
                    printf("O lutador %s do jogador %i defendeu %.2f e recebeu %.2f de dano!\n", jogador_defensor[atacado].nome, numero_jogador_defensor, acao_defensor, dano);
                    atualizar_vida(jogador_defensor, atacado, dano, numero_jogador_defensor);
                }
            }
            atacante++;
        }
        else
        {
            if (jogador_atacante[atacante].vida > 0)
            {
                printf("O lutador %s não pode atacar nesse turno!\n", jogador_atacante[atacante].nome);
                jogador_atacante[atacante].ativo = 1;
            }
            else
            {
                printf("O lutador %s já está morto!\n", jogador_atacante[atacante].nome);
            }
            atacante++;
        }
    }
}

void jogar()
{
    Jogador jogador1[4];
    Jogador jogador2[4];

    inicializar_time(jogador1, 4);
    imprimir_equipe(jogador1, 4);

    printf("\n");

    inicializar_time(jogador2, 4);
    imprimir_equipe(jogador2, 4);

    int numero_jogador = (rand() % 2) + 1;

    do
    {
        if (numero_jogador == 1)
        {
            ataque(jogador1, jogador2, 4, numero_jogador);
            numero_jogador++;
        }
        else
        {
            ataque(jogador2, jogador1, 4, numero_jogador);
            numero_jogador--;
        }

    }while (vida_jogador1 > 0 && vida_jogador2 > 0);
}

void main()
{
    srand(time(NULL));
    jogar();
}