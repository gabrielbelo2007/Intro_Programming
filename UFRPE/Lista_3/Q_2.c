//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>

void main()
{
    int inteiros[8];
    const int tamanho = sizeof(inteiros)/sizeof(int);

    for (int index = 0; index < tamanho; index++)
    {
        scanf("%i", &inteiros[index]);
        getchar();
    }

    int maior = inteiros[0];
    int menor = inteiros[0];
    int posicao_menor = 0;
    int posicao_maior = 0;

    for (int index = 1; index < tamanho; index++)
    {
        if (menor > inteiros[index])
        {
            menor = inteiros[index];
            posicao_menor = index;
        }

        if (inteiros[index] > maior)
        {
            maior = inteiros[index];
            posicao_maior = index;
        }
    }

    printf("O menor valor foi: %i na posição: %i. \nO maior valor foi: %i na posição: %i.",  menor, posicao_menor, maior, posicao_maior);
}