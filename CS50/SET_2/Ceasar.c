#include <stdio.h>
#include <string.h>
#include <ctype.h>

void ceasar(char text[], int size, int k);

int main(void)
{
    char text[100];
    int k = 0;
    printf("Digite o texto a ser criptografado: ");
    fgets(text, sizeof(text), stdin);

    printf("Digite a chave: ");
    scanf("%i", &k);

    ceasar(text, (strlen(text) - 1), k);
}

void ceasar(char text[], int size, int k)
{
    int ceasar_int[size];

    for (int i = 0; i < size; i++)
    {
        int ci = 0;
        if (isupper(text[i]) != 0)
        {
            int position_table = (int) text[i] + k;
            if (position_table > 89)
            {
                ci = position_table % 89 + 64;
            }
            else
            {
                ci = position_table;
            }
            ceasar_int[i] = ci;
        }
        else if (islower(text[i]) != 0)
        {
            int position_table = (int) text[i] + k;
            if (position_table > 122)
            {
                ci = position_table % 122 + 96;
            }
            else
            {
                ci = position_table;
            }
            ceasar_int[i] = ci;
        }
        else
        {
            ceasar_int[i] = (int) text[i];
        }
    }

    for (int i = 0; i < size; i++)
    {
        printf("%c", ceasar_int[i]);
    }
}