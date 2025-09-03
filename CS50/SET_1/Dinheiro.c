#include <math.h>
#include <stdio.h>

void cash();

int main(void)
{
    cash();
}

void cash()
{
    float debt = 0;
    do
    {
        printf("Troca devida: ");
        scanf("%f", &debt);
        getchar();
    }while (debt <= 0);

    int debt_cents = round(debt * 100);
    int qtd_coins = 0;

    do
    {
        if ((debt_cents - 25) >= 0)
        {
            qtd_coins++;
            debt_cents -= 25;
        }
        else if ((debt_cents - 10) >= 0)
        {
            qtd_coins++;
            debt_cents -= 10;
        }
        else if ((debt_cents - 5) >= 0)
        {
            qtd_coins++;
            debt_cents -= 5;
        }
        else
        {
            qtd_coins++;
            debt_cents -= 1;
        }
    }while (debt_cents > 0);

    printf("%i", qtd_coins);
}