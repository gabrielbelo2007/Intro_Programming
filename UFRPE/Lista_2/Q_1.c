//
// Created by gabrielbelo on 28/05/25.
//

#include <stdio.h>

void main()
{
    float N;
    int quadrado_proximo = 0;
    float estimativa_inicial = 0;

    printf("Digite um número para acessar sua raiz: ");
    scanf("%f", &N);

    while (quadrado_proximo <= N) // N = 5
    {
        estimativa_inicial++;
        quadrado_proximo = (estimativa_inicial + 1) * (estimativa_inicial + 1);
    }
    quadrado_proximo = estimativa_inicial * estimativa_inicial;

    if (quadrado_proximo == N)
    {
        printf("A raiz desse número é: %.0f", estimativa_inicial);
    }
    else
    {
        float estimativa_proxima = (estimativa_inicial + N / estimativa_inicial) / 2;
        printf("A raiz desse número é: %.2f", estimativa_proxima);
    }
}