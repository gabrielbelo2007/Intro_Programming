#include <stdio.h>

void main()
{
    int tamanho_usado = 3;
    int filmes[3];

    filmes[0] = 2;
    filmes[1] = 1;
    filmes[2] = 3;

    int indice_ordenacao = -1;
    for (int indice_desordenado = 0; indice_desordenado < tamanho_usado; indice_desordenado++)
    {
        int mudou = 0;
        int alugueis_temp = filmes[indice_desordenado]; // 2

        for (int indice_ordenado = 0; indice_ordenado < tamanho_usado; indice_ordenado++)
        {
            if (filmes[indice_ordenado] > alugueis_temp)
            {
                alugueis_temp = filmes[indice_ordenado];
                indice_ordenacao = indice_ordenado;
                mudou = 1;
            }
        }
        indice_ordenacao = (mudou == 0) ? indice_desordenado : indice_ordenacao;
        printf("%i", filmes[indice_ordenacao]);
        filmes[indice_ordenacao] = -1;
    }
}
