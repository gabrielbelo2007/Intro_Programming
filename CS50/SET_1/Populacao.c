#include <stdio.h>

void crescimento();

int main(void)
{
    crescimento();
}

void crescimento()
{
    int initial_value = 0;
    int final_value = 0;
    do
    {
        printf("Digite o tamanho inicial da população: ");
        scanf("%i", &initial_value);
        getchar();
    }while (initial_value < 9);

    do
    {
        printf("Digite o tamanho final da população: ");
        scanf("%i", &final_value);
        getchar();
    }while (final_value < initial_value);

    int years = 0;
    int remote_value = initial_value;
    while (remote_value < final_value)
    {
        years++;
        int new_lhamas = remote_value / 3;
        int die_lhamas = remote_value / 4;

        remote_value += (new_lhamas - die_lhamas);
    }

    printf("Start Size: %i\n", initial_value);
    printf("End Size: %i\n", final_value);
    printf("Years: %i\n", years);
}