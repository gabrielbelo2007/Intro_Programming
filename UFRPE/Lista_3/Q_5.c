//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>

void main()
{
    int inteiros[15];
    int tamanho = sizeof(inteiros)/sizeof(int);
    int total = 0;

    for (int index = 0; index < tamanho; index++)
    {
        scanf("%i", &inteiros[index]);
        total += inteiros[index];
        getchar();
    }

    const int media = total / tamanho;
    int maiores_media = 0;
    for (int index = 0; index < tamanho; index++)
    {
        if (inteiros[index] > media)
        {
            maiores_media++;
        }
    }

    printf("%i valores foram acima da média", maiores_media);
}