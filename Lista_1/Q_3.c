//
// Created by gabrielbelo on 15/05/25.
//

#include <stdio.h>

void main()
{
    int numero;
    printf("Digite um número: ");
    scanf("%i", &numero);

    int n_numero_menos2 = 0; // 2 index a menos
    int n_numero_menos1 = 1; // 1 index a menos
    if (numero == 1)
    {
        printf("%i", n_numero_menos2);
    }
    else if (numero == 2)
    {
        printf("%i", n_numero_menos1);
    }
    else if (numero >= 3)
    {
        int n_numero = 0;
        for (int x = 3; x <= numero; x++)
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
