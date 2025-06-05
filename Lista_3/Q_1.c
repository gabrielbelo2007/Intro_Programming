//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>

void main()
{
    int inteiros[10];
    const int tamanho = sizeof(inteiros)/sizeof(int);

    int index = 0;
    int soma = 0;
    for (int x=0; x < tamanho; x++)
    {
        scanf("%i", &inteiros[index]);
        getchar();

        soma+=inteiros[index];
        index++;
    }

    printf("%i", soma);
}
