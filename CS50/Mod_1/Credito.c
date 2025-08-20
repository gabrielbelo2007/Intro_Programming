#include <stdio.h>
#include <string.h>

void credit_validation();

int main(void)
{
    credit_validation();
}

void credit_validation()
{
    char credit_number[17];
    printf("Digite o número do cartão: ");
    scanf("%s", credit_number);
    getchar();

    if (16 < strlen(credit_number) || strlen(credit_number) < 13)
    {
        printf("INVALID");
    }
    else
    {
        int credit_sum = 0;
        for (int i = (strlen(credit_number) - 2); i >= 0; i -= 2)
        {
            int numero = credit_number[i] - '0';
            int resultado = numero * 2;

            if (resultado >= 10)
            {
                credit_sum += resultado / 10;
                credit_sum += resultado % 10;
            }
            else
            {
                credit_sum += resultado;
            }
        }

        for (int i = (strlen(credit_number) - 1); i >= 0; i -= 2)
        {
            int numero = credit_number[i] - '0';
            credit_sum += numero;
        }

        if (credit_sum % 10 == 0)
        {
            if (credit_number[0] == '4')
            {
                printf("Visa");
            }
            else if (credit_number[0] == '5')
            {
                switch (credit_number[1])
                {
                case '1':
                    printf("MasterCard");
                    break;
                case '2':
                    printf("MasterCard");
                    break;
                case '3':
                    printf("MasterCard");
                    break;
                case '4':
                    printf("MasterCard");
                    break;
                case '5':
                    printf("MasterCard");
                    break;
                default:
                    printf("Cartão inválido!");
                }
            }
            else if (credit_number[0] == '3')
            {
                switch (credit_number[1])
                {
                case '4':
                    printf("American Express");
                    break;
                case '7':
                    printf("American Express");
                    break;
                default:
                    printf("Cartão inválido!");
                }
            }
        }
        else
        {
            printf("Número inválido!");
        }
    }
}