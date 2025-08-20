//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>
#include <string.h>

void main()
{
    char texto[100];
    scanf("%s", &texto);
    int tamanho = strlen(texto);

    int qtd_vogais = 0;
    for (int index = 0; index < tamanho; index++)
    {
        switch (texto[index])
        {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
            qtd_vogais++;
            break;
        }
    }

    printf("A quantidade de vogais foi: %i", qtd_vogais);
}