#include <stdio.h>

void mario();
void mario_challenge();

int main(void)
{
    // mario();
    mario_challenge();
}

void mario()
{
    int size_pyramid = 0;
    do
    {
        printf("Size: ");
        scanf("%i", &size_pyramid);
        getchar();
    }
    while (size_pyramid < 1 || size_pyramid > 8);

    int blank_space = (size_pyramid - 1);
    int height = 0;
    for (int i = 0; i < size_pyramid; i++)
    {
        for (int j = 0; j < blank_space; j++)
        {
            printf(" ");
        }
        blank_space--;

        for (int z = 0; z <= height; z++)
        {
            printf("#");
        }
        height++;
        printf("\n");
    }
}

void mario_challenge()
{
    int size_pyramid = 0;
    do
    {
        printf("Size: ");
        scanf("%i", &size_pyramid);
        getchar();
    }
    while (size_pyramid < 1 || size_pyramid > 8);

    int blank_space = (size_pyramid - 1);
    int height = 0;
    for (int linha = 0; linha < size_pyramid; linha++)
    {
        for (int j = 0; j < blank_space; j++)
        {
            printf(" ");
        }
        blank_space--;

        for (int z = 0; z <= height; z++)
        {
            printf("#");
        }
        height++;

        printf(" ");

        for (int w = 0; w < height; w++)
        {
            printf("#");
        }
        printf("\n");
    }
}

