//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>
#include <string.h>

void main()
{
    char texto[];
    scanf("%s", &texto);

    int tamanho = strlen(texto);
    char texto_invertido[100];
    int index_invertido = tamanho - 1;
    for (int index = 0; index < tamanho; index++)
    {
        texto_invertido[index_invertido] = texto[index];
        index_invertido--;
    }

    if (strcmp(texto_invertido, texto) == 0)
    {
        printf("O texto '%s' é um palindromo!", texto);
    }
    else
    {
        printf("O texto '%s' não é um palindromo!", texto);
    }
}