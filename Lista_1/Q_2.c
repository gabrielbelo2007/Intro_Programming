//
// Created by gabrielbelo on 15/05/25.
//
#include <stdio.h>

void main()
{
    int numero;

    printf("Digite um número: ");
    scanf("%i", &numero);

    int inicial = 1;
    int final =  numero;
    int alternar = numero / 2;
    for (inicial; inicial <= alternar; inicial++)
    {
        printf("%i", inicial);
        printf("%i", final);
        final--;
    }

    if (numero % 2 != 0)
    {
        printf("%i", inicial);
    }
}
