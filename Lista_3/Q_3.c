//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>

void main()
{
    int inteiros[10];
    const int tamanho = sizeof(inteiros)/sizeof(int);

    for (int index = 0; index < tamanho; index++)
    {
        scanf("%i", &inteiros[index]);
        getchar();
    }

    int valor_verificar;
    printf("Quer saber se está registrado: ");
    scanf("%i", &valor_verificar);

    int registrado = 0;
    for (int index = 0; index < tamanho; index++)
    {
        int numero_registrado = inteiros[index];
        if (valor_verificar == numero_registrado)
        {
            printf("O valor: %i está salvo no array, na posição: %i.", valor_verificar, index);
            registrado = 1;
            break;
        }
    }

    if (registrado == 0)
    {
        printf("O valor: %i, não está salvo no array.", valor_verificar);
    }
}