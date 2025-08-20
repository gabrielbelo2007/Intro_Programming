//
// Created by gabrielbelo on 04/06/25.
//

#include <stdio.h>
#include <string.h>

void main()
{
    char palavra_secreta[100] = "abacate";
    int tamanho_secreta = strlen(palavra_secreta);
    char palavra_descoberta[100] = "";
    int tentativas = tamanho_secreta / 2;

    for (int index = 0; index < tamanho_secreta; index++)
    {
        palavra_descoberta[index] = '_';
    }
    palavra_descoberta[tamanho_secreta] = '\0';

    int tamanho_descoberta = strlen(palavra_descoberta);
    printf("A palavra secreta tem %i caracteres: %s\n Tentativas: %i", tamanho_descoberta, palavra_descoberta, tentativas);

    char letras_testadas[100] = "\0";
    int index_letras = 0;
    while (strcmp(palavra_descoberta, palavra_secreta) != 0 && tentativas > 0)
    {
        char tentativa_letra;
        printf("\n\nDigite uma letra: ");
        scanf("%c", &tentativa_letra);
        getchar();

        if (strchr(letras_testadas, tentativa_letra) == NULL)
        {
            letras_testadas[index_letras] = tentativa_letra;
            letras_testadas[index_letras + 1] = '\0';
            index_letras++;

            if (strchr(palavra_secreta, tentativa_letra))
            {
                for (int index = 0; index < tamanho_secreta; index++)
                {
                    if (palavra_secreta[index] == tentativa_letra)
                    {
                        palavra_descoberta[index] = tentativa_letra;
                    }
                }
                printf("Acertou!\nA palavra descoberta atual: %s", palavra_descoberta);
            }
            else
            {
                tentativas--;
                printf("Errou! Tentativa(s) restante(s): %i \nA palavra descoberta atual: %s", tentativas, palavra_descoberta);
            }
        }
        else
        {
            printf("A letra: '%c' já foi usada! Escolha outra.", tentativa_letra);
        }
    }

    if (tentativas > 0)
    {
        printf("\nParabéns você descobriu a palavra secreta: %s", palavra_secreta);
    }
    else
    {
        printf("\nVocê não conseguiu descobrir a palavra secreta: %s", palavra_secreta);
    }
}