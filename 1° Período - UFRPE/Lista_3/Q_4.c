//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>

void main()
{
    int inteiros[5];
    int tamanho = sizeof(inteiros)/sizeof(int);

    for (int index = 0; index < tamanho; index++)
    {
        scanf("%i", &inteiros[index]);
        getchar();
    }

    printf("Exibindo na ordem inversa: ");
    for (int index = (tamanho - 1); index >= 0; index--)
    {
        printf("%i ", inteiros[index]);
    }
}