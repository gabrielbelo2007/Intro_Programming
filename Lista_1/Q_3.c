//
// Created by gabrielbelo on 15/05/25.
//

#include <stdio.h>

void main()
{
    int numero;
    printf("Digite um número: ");
    scanf("%i", &numero);

    if (numero == 1)
    {
        printf("%i", 0);
    }
    else if (numero == 2 || numero == 3)
    {
        printf("%i", 1);
    }
    else if (numero > 3)
    {
        int n_numero_menos2 = 1;
        int n_numero_menos1 = 1;
        int n_numero;
        for (int x = 3; x < numero; x++)
        {
            n_numero = n_numero_menos2 + n_numero_menos1;
            n_numero_menos2 = n_numero_menos1;
            n_numero_menos1 = n_numero;
        }
        printf("%i", n_numero);
    }
    else
    {
        printf("Digite um numero valido");
    }
}
