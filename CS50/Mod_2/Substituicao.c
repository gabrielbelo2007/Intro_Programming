#include <stdio.h>
#include <string.h>
#include <ctype.h>

void encrypt(char alphabet[], char text[]);

int main(void)
{
    char new_alphabet[27];
    do
    {
        printf("Digite a chave de substituição: ");
        fgets(new_alphabet, sizeof(new_alphabet), stdin);
        getchar();
    }while(strlen(new_alphabet) != 26);

    char text[100];
    printf("Digite o texto para ser criptografado: ");
    fgets(text, sizeof(text), stdin);

    encrypt(new_alphabet, text);
}

void encrypt(char alphabet[], char text[])
{
    char text_encrypted[strlen(text)];

    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] != ',' && text[i] != ' ')
        {
            char upper_c = toupper(text[i]);
            int position_c = upper_c - 65;

            char new_c = alphabet[position_c];
            if (islower(text[i]) != 0)
            {
                text_encrypted[i] = tolower(new_c);
            }
            else
            {
                text_encrypted[i] = new_c;
            }
        }
        else
        {
            text_encrypted[i] = text[i];
        }
    }
    printf("%s", text_encrypted);
}