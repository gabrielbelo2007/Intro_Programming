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
    char frase_sem_espaco[100];
    int index_sem_espaco = 0;
    for (int index = 0; index < tamanho; index++)
    {
        if (frase[index] != branco)
        {
            frase_sem_espaco[index_sem_espaco] = frase[index];
            index_sem_espaco++;
        }
    }

    printf("%s", frase_sem_espaco);
}