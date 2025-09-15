#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct
{
    int vida;
    float taxa_raiva;
    int l_eleven;
    int c_eleven;
}Eleven;

typedef struct
{
    int l_will;
    int c_will;
}Will;

typedef struct
{
    int l_demodog;
    int c_demodog;
}Demodog;

Eleven inicializar_eleven()
{
    Eleven eleven;

    eleven.vida = 100;
    eleven.taxa_raiva = 0;
    eleven.l_eleven = rand() % 3;
    eleven.c_eleven = rand() % 3;

    return eleven;
}

void inicializar_sala(char sala[][3], int l_eleven, int c_eleven)
{
    for (int l = 0; l < 3; l++)
    {
        for (int c = 0; c < 3; c++)
        {
            sala[l][c] = '_';
        }
    }

    sala[l_eleven][c_eleven] = 'E';
}

void imprimir_sala(char sala[][3])
{
    for (int l = 0; l < 3; l++)
    {
        for (int c = 0; c < 3; c++)
        {
            printf("%c", sala[l][c]);
        }
        printf("\n");
    }
    printf("\n");
}

int abrir_portal(char sala[][3], Eleven *eleven)
{
    eleven->taxa_raiva = rand() % 101;

    if (eleven->taxa_raiva >= 60)
    {
        int l_portal;
        int c_portal;
        do
        {
            l_portal = rand() % 3;
            c_portal = rand() % 3;
        }while (l_portal == eleven->l_eleven && c_portal == eleven->c_eleven);

        sala[l_portal][c_portal] = 'O';
        return 1;
    }

    eleven->vida -= 20;
    return 0;
}

int movimentar_eleven_sala(char sala[][3], Eleven *eleven)
{
    char movimento;
    printf("Cima(c) | Baixo(b) | Esquerda(e) | Direita(d): ");
    scanf(" %c", &movimento);
    getchar();

    switch (movimento)
    {
        case 'c':
            if (eleven->l_eleven > 0)
            {
                sala[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven -= 1;
            }
            else
            {
                printf("Movimento Bloqueado!\n");
            }
        break;

        case 'b':
            if (eleven->l_eleven < 2)
            {
                sala[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven += 1;
            }
            else
            {
                printf("Movimento Bloqueado!\n");
            }
        break;

        case 'e':
            if (eleven->c_eleven > 0)
            {
                sala[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven -= 1;
            }
            else
            {
                printf("Movimento Bloqueado!\n");
            }
        break;

        case 'd':
            if (eleven->c_eleven < 2)
            {
                sala[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven += 1;
            }
            else
            {
                printf("Movimento Bloqueado!\n");
            }
        break;
    }
    if (sala[eleven->l_eleven][eleven->c_eleven] == 'O')
    {
        return 1;
    }
    printf("\n");
    sala[eleven->l_eleven][eleven->c_eleven] = 'E';
    return 0;
}

Will inicializar_will()
{
    Will will;

    will.l_will = rand() % 10;
    will.c_will = rand() % 10;

    return will;
}

void inicializar_demodog(Demodog demodogs[])
{
    for (int demodog = 0; demodog < 4; demodog++)
    {
        if (demodog > 0)
        {
            int c_demodog = rand() % 10;
            int l_demodog = rand() % 10;
            while (c_demodog == demodogs[demodog - 1].c_demodog && l_demodog == demodogs[demodog - 1].l_demodog)
            {
                c_demodog = rand() % 10;
                l_demodog = rand() % 10;
            }
            demodogs[demodog].c_demodog = c_demodog;
            demodogs[demodog].l_demodog = l_demodog;
        }
        else
        {
            demodogs[demodog].c_demodog = rand() % 10;
            demodogs[demodog].l_demodog = rand() % 10;
        }
    }
}

void inicializar_mundo_invertido(char mundo_invertido[][10], Eleven *eleven, Will *will, Demodog demodogs[])
{
    for (int l = 0; l < 10; l++)
    {
        for (int c = 0; c < 10; c++)
        {
            mundo_invertido[l][c] = '_';
        }
    }

    eleven->l_eleven = rand() % 10;
    eleven->c_eleven = rand() % 10;
    mundo_invertido[eleven->l_eleven][eleven->c_eleven] = 'E';

    while (mundo_invertido[will->l_will][will->c_will] != '_')
    {
        will->l_will = rand() % 10;
        will->c_will = rand() % 10;
    }
    mundo_invertido[will->l_will][will->c_will] = 'W';

    int l_portal;
    int c_portal;
    do
    {
        l_portal = rand() % 10;
        c_portal = rand() % 10;
     }while (mundo_invertido[l_portal][c_portal] != '_');
    mundo_invertido[l_portal][c_portal] = 'O';

    for (int arvores = 0; arvores < 10; arvores++)
    {
        int l_arvore;
        int c_arvore;
        do
        {
            l_arvore = rand() % 10;
            c_arvore = rand() % 10;
        }while (mundo_invertido[l_arvore][c_arvore] != '_');
        mundo_invertido[l_arvore][c_arvore] = 'I';
    }

    for (int carros = 0; carros < 5; carros++)
    {
        int l_carros;
        int c_carros;
        do
        {
            l_carros = rand() % 10;
            c_carros= rand() % 10;
        }while (mundo_invertido[l_carros][c_carros] != '_');
        mundo_invertido[l_carros][c_carros] = '>';
    }

    for (int casas_abandonadas = 0; casas_abandonadas < 5; casas_abandonadas++)
    {
        int l_casa;
        int c_casa;
        do
        {
            l_casa = rand() % 10;
            c_casa = rand() % 10;
        }while (mundo_invertido[l_casa][c_casa] != '_');
        mundo_invertido[l_casa][c_casa] = 'A';
    }

    for (int panquecas = 0; panquecas < 10; panquecas++)
    {
        int l_panqueca;
        int c_panqueca;
        do
        {
            l_panqueca = rand() % 10;
            c_panqueca = rand() % 10;
        }while (mundo_invertido[l_panqueca][c_panqueca] != '_');
        mundo_invertido[l_panqueca][c_panqueca] = 'C';
    }

    for (int demodog = 0; demodog < 4; demodog++)
    {
        while (mundo_invertido[demodogs[demodog].l_demodog][demodogs[demodog].c_demodog] != '_')
        {
            demodogs[demodog].l_demodog = rand() % 10;
            demodogs[demodog].c_demodog = rand() % 10;
        }
    }
}

void imprimir_mundo_invertido(char mundo_invertido[][10])
{
    printf("\n");
    for (int l = 0; l < 10; l++)
    {
        for (int c = 0; c < 10; c++)
        {
            printf("%c", mundo_invertido[l][c]);
        }
        printf("\n");
    }
    printf("\n");
}

int checar_demodogs(Demodog demodogs[], int l_mundo, int c_mundo)
{
    for (int demodog = 0; demodog < 4; demodog++)
    {
        int c_demodog = demodogs[demodog].c_demodog;
        int l_demodog = demodogs[demodog].l_demodog;

        if (l_demodog == l_mundo && c_demodog == c_mundo)
        {
            return 1;
        }
    }
    return 0;
}

void movimentar_will(char mundo_invertido[][10], int *l_will, int *c_will, Demodog demodogs[])
{
    int movimento = rand() % 4;

    switch (movimento)
    {
    // cima
      case 0:
        if (*l_will > 0)
        {
            char prox_posicao_will = mundo_invertido[*l_will - 1][*c_will];
            int encontrou_demodog = checar_demodogs(demodogs, (*l_will-1), *c_will);

            if(prox_posicao_will == '_' && !encontrou_demodog)
            {
                mundo_invertido[*l_will][*c_will] = '_';
                *l_will -= 1;
            }
        }
        break;
    // baixo
        case 1:
            if (*l_will < 9)
            {
                char prox_posicao_will = mundo_invertido[*l_will + 1][*c_will];
                int encontrou_demodog = checar_demodogs(demodogs, (*l_will+1), *c_will);

                if(prox_posicao_will == '_' && !encontrou_demodog)
                {
                    mundo_invertido[*l_will][*c_will] = '_';
                    *l_will += 1;
                }
            }
        break;
    // esquerda
        case 2:
            if (*c_will > 0)
            {
                char prox_posicao_will = mundo_invertido[*l_will][*c_will - 1];
                int encontrou_demodog = checar_demodogs(demodogs, *l_will, (*c_will-1));

                if(prox_posicao_will == '_' && !encontrou_demodog)
                {
                    mundo_invertido[*l_will][*c_will] = '_';
                    *c_will -= 1;
                }
            }
        break;
    // direita
        case 3:
            if (*c_will < 9)
            {
                char prox_posicao_will = mundo_invertido[*l_will][*c_will + 1];
                int encontrou_demodog = checar_demodogs(demodogs, *l_will, (*c_will+1));

                if(prox_posicao_will == '_' && !encontrou_demodog)
                {
                    mundo_invertido[*l_will][*c_will] = '_';
                    *c_will += 1;
                }
            }
        break;
    }
    mundo_invertido[*l_will][*c_will] = 'W';
}

int movimentar_eleven_mundo_invertido(char mundo_invertido[][10], Eleven *eleven, Demodog demodogs[], Will *will, int *resgatou)
{
    char movimento;
    printf("Cima(c) | Baixo(b) | Esquerda(e) | Direita(d): ");
    scanf("%c", &movimento);
    getchar();

    switch (movimento)
    {
    case 'c':
        if (eleven->l_eleven > 0)
        {
            char prox_posicao_eleven = mundo_invertido[eleven->l_eleven - 1][eleven->c_eleven];
            int encontrou_demodog = checar_demodogs(demodogs, (eleven->l_eleven-1), eleven->c_eleven);
            if (encontrou_demodog)
            {
                eleven->vida -= 10;
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven -= 1;
            }

            else if (prox_posicao_eleven == 'W')
            {
                printf("Will: você me encontrou Eleven! Vamos embora daqui!\n\n");
                *resgatou = 1;
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven -= 1;
            }
            else if(prox_posicao_eleven == '_' || prox_posicao_eleven == 'O')
            {
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven -= 1;
            }
            else if (prox_posicao_eleven == 'I' || prox_posicao_eleven == 'A' || prox_posicao_eleven == '>')
            {
                printf("Obstáculo no caminho!\n");
            }
            else if (prox_posicao_eleven == 'C')
            {
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven -= 1;

                eleven->vida += (eleven->vida < 100) ? 5 : 0;
            }
        }
        else
        {
            printf("Movimento Bloqueado!\n");
        }
        break;

    case 'b':
        if (eleven->l_eleven < 9)
        {
            char prox_posicao_eleven = mundo_invertido[eleven->l_eleven + 1][eleven->c_eleven];
            int encontrou_demodog = checar_demodogs(demodogs, (eleven->l_eleven+1), eleven->c_eleven);
            if (encontrou_demodog)
            {
                eleven->vida -= 10;
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven += 1;
            }

            else if (prox_posicao_eleven == 'W')
            {
                printf("Will: você me encontrou Eleven! Vamos embora daqui!\n\n");
                *resgatou = 1;
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven += 1;
            }
            else if(prox_posicao_eleven == '_' || prox_posicao_eleven == 'O')
            {
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven += 1;
            }
            else if (prox_posicao_eleven == 'I' || prox_posicao_eleven == 'A' || prox_posicao_eleven == '>')
            {
                printf("Obstáculo no caminho!\n");
            }
            else if (prox_posicao_eleven == 'C')
            {
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->l_eleven += 1;

                eleven->vida += (eleven->vida < 100) ? 5 : 0;
            }
        }
        else
        {
            printf("Movimento Bloqueado!\n");
        }
        break;

    case 'e':
        if (eleven->c_eleven > 0)
        {
            char prox_posicao_eleven = mundo_invertido[eleven->l_eleven][eleven->c_eleven - 1];
            int encontrou_demodog = checar_demodogs(demodogs, eleven->l_eleven, (eleven->c_eleven-1));
            if (encontrou_demodog)
            {
                eleven->vida -= 10;
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven -= 1;
            }

            else if (prox_posicao_eleven == 'W')
            {
                printf("Will: você me encontrou Eleven! Vamos embora daqui!\n\n");
                *resgatou = 1;
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven -= 1;
            }
            else if(prox_posicao_eleven == '_' || prox_posicao_eleven == 'O')
            {
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven -= 1;
            }
            else if (prox_posicao_eleven == 'I' || prox_posicao_eleven == 'A' || prox_posicao_eleven == '>')
            {
                printf("Obstáculo no caminho!\n");
            }
            else if (prox_posicao_eleven == 'C')
            {
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven -= 1;

                eleven->vida += (eleven->vida < 100) ? 5 : 0;
            }
        }
        else
        {
            printf("Movimento Bloqueado!\n");
        }
        break;

    case 'd':
        if (eleven->c_eleven < 9)
        {
            char prox_posicao_eleven = mundo_invertido[eleven->l_eleven][eleven->c_eleven + 1];
            int encontrou_demodog = checar_demodogs(demodogs, eleven->l_eleven, (eleven->c_eleven+1));
            if (encontrou_demodog)
            {
                eleven->vida -= 10;
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven += 1;
            }

            else if (prox_posicao_eleven == 'W')
            {
                printf("Will: você me encontrou Eleven! Vamos embora daqui!\n\n");
                *resgatou = 1;
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven += 1;
            }
            else if(prox_posicao_eleven == '_' || prox_posicao_eleven == 'O')
            {
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven += 1;
            }
            else if (prox_posicao_eleven == 'I' || prox_posicao_eleven == 'A' || prox_posicao_eleven == '>')
            {
                printf("Obstáculo no caminho!\n");
            }
            else if (prox_posicao_eleven == 'C')
            {
                mundo_invertido[eleven->l_eleven][eleven->c_eleven] = '_';
                eleven->c_eleven += 1;

                eleven->vida += (eleven->vida < 100) ? 5 : 0;
            }
        }
        else
        {
            printf("Movimento Bloqueado!\n");
        }
        break;

    default:
        printf("Digite um movimento válido!");
    }

    if (mundo_invertido[eleven->l_eleven][eleven->c_eleven] == 'O' && *resgatou)
    {
        return 1;
    }
    printf("\n");
    mundo_invertido[eleven->l_eleven][eleven->c_eleven] = 'E';
    if (!(*resgatou))
    {
        movimentar_will(mundo_invertido, &will->l_will, &will->c_will, demodogs);
    }
    return 0;
}

int main()
{
    srand(time(NULL));

    // Sala 3x3

    char sala[3][3];
    Eleven eleven = inicializar_eleven();

    inicializar_sala(sala, eleven.l_eleven, eleven.c_eleven);
    imprimir_sala(sala);

    int portal_aberto = 0;
    printf("Abra o portal para o mundo invertido, Will espera por você!\n");
    do
    {
        char o;
        printf("Vida atual: %i\n", eleven.vida);
        printf("Taxa de raiva: %.2f%%\n", eleven.taxa_raiva);
        printf("Canalizar sua raiva?(s) ");
        scanf(" %c", &o);
        getchar();

        portal_aberto = abrir_portal(sala, &eleven);
        if (portal_aberto == 0 && eleven.vida > 0)
        {
            printf("\nVocê falhou! Vamos logo Will está esperando!\n");
        }
        printf("\n");
    }while (!portal_aberto && eleven.vida > 0);

    if (portal_aberto && eleven.vida > 0)
    {
        int atravessou_portal;
        do
        {
            imprimir_sala(sala);
            atravessou_portal = movimentar_eleven_sala(sala, &eleven);
        }while(!atravessou_portal);
        atravessou_portal = 0;

        // Mundo Invertido

        printf("\nBem-vinda ao mundo invertido, ache Will e retorne em segurança!\n");

        char mundo_invertido[10][10];
        Demodog demodogs[4];
        inicializar_demodog(demodogs);
        Will will = inicializar_will();

        inicializar_mundo_invertido(mundo_invertido, &eleven, &will, demodogs);
        int resgatou_will = 0;
        do
        {
            printf("Vida: %i\n\n", eleven.vida);
            imprimir_mundo_invertido(mundo_invertido);
            atravessou_portal = movimentar_eleven_mundo_invertido(mundo_invertido, &eleven, demodogs, &will, &resgatou_will);
        }while (eleven.vida > 0 && !atravessou_portal);

        if (eleven.vida > 0 && atravessou_portal)
        {
            printf("Parabéns o resgate foi um sucesso!");
        }
        else
        {
            printf("Will e Eleven se perderam no Mundo Invertido...");
        }
    }
    else
    {
        printf("\nVocê não conseguiu salvar Will...");
    }
    return 1;
}