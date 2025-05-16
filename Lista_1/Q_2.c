//
// Created by gabrielbelo on 15/05/25.
//
#include <stdio.h>

void main()
{
    int numero;

    printf("Digite um número: ");
    scanf("%i", &numero);

    int x = 1;
    int cond = numero / 2;
    for (x; x <= cond; x++)
    {
        printf("%i", x);
        printf("%i", numero);
        numero--;
    }

    if (numero % 2 != 0)
    {
        printf("%i", x);
    }
}
