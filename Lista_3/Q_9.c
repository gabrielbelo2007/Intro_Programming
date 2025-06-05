//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>
#include <string.h>

void main()
{
    char frase[100];
    scanf("%[^\n]%*c", frase);
    int tamanho = strlen(frase);

    char branco = ' ';
    int qtd_palavras = 0;
    for (int index = 0; index < tamanho; index++)
    {
        if (frase[index] == branco)
        {
            qtd_palavras++;
        }
    }

    qtd_palavras++;
    printf("O número de palavra(s) na frase: '%s' é %i palavra(s)!", frase, qtd_palavras);
}