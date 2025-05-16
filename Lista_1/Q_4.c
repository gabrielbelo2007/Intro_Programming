//
// Created by gabrielbelo on 16/05/25.
//

#include <endian.h>
#include <stdio.h>

void main()
{
    int numero;

    printf("Tamanho do quadrado: ");
    scanf("%i", &numero);

    if (numero % 2 == 0)
    {
        int espaco_meio =  numero - 2;
        int espaco_inicio = 0;

        // Metade - 1
        for (int tamanho = numero / 2; tamanho > 1; tamanho--)
        {
            printf("x");
            for (int x = 0; x < espaco_meio; x++)
            {
                printf(" ");
            }
            espaco_meio -= 2;
            printf("x\n");

            ++espaco_inicio;
            for (int y = 0; y < espaco_inicio; y++)
            {
                printf(" ");
            }
        }

        // Metade
        printf("xx\n");

        // Fazer da metade para baixo
        for (int tamanho = numero / 2; tamanho > 0; tamanho--)
        {
            for (int y = 0; y < espaco_inicio; y++)
            {
                printf(" ");
            }
            --espaco_inicio;

            printf("x");
            for (int x = 0; x < espaco_meio; x++)
            {
                printf(" ");
            }
            printf("x\n");
            espaco_meio += 2;
        }
    }

    else
    {
        int espaco_meio = numero - 2;
        int espaco_inicio = 0;

        // Metade - 1
        for (int tamanho = numero / 2; tamanho > 0; tamanho--)
        {

            printf("x");
            for (int x = 0; x < espaco_meio; x++)
            {
                printf(" ");
            }
            printf("x\n");

            if (espaco_meio > 1)
            {
                espaco_meio -= 2;
            }

            espaco_inicio++;
            for (int y = 0; y < espaco_inicio; y++)
            {
                printf(" ");
            }
        }

        //Metade
        printf("x\n");

        //Metade para baixo
        for (int tamanho = numero / 2; tamanho > 0; tamanho--)
        {
            espaco_inicio--;
            for (int y = 0; y < espaco_inicio; y++)
            {
                printf(" ");
            }

            printf("x");
            for (int x = 0; x < espaco_meio; x++)
            {
                printf(" ");
            }
            printf("x\n");
            espaco_meio += 2;
        }
    }
}