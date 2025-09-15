//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>
#include <string.h>

void main()
{
    char frase1[100];
    char frase2[100];

    printf("Escreva a frase 1: ");
    scanf("%s", frase1);

    printf("Escreva a frase 2: ");
    scanf("%s", frase2);

    strcat(frase1, frase2);
    printf("%s", frase1);
}