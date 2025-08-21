#include <stdio.h>
#include <string.h>
#include <ctype.h>

typedef struct
{
    int point;
    char letra;
} Score;

int compute_score(char words[][21]);

int main(void)
{
    char words[2][21];

    printf("Player 1: ");
    scanf("%s", words[0]);
    getchar();

    printf("Player 2: ");
    scanf("%s", words[1]);
    getchar();

    int result = compute_score(words);
    if (result == 1)
    {
        printf("Player 1 Wins!");
    }
    else if (result == 2)
    {
        printf("Player 2 Wins!");
    }
    else
    {
        printf("Tie!");
    }
}

int compute_score(char words[][21])
{
    Score points[] = {
        {1, 'a'},
        {3, 'b'},
        {3, 'c'},
        {2, 'd'},
        {1, 'e'},
        {4, 'f'},
        {2, 'g'},
        {4, 'h'},
        {1, 'i'},
        {8, 'j'},
        {5, 'k'},
        {1, 'l'},
        {3, 'm'},
        {1, 'n'},
        {1, 'o'},
        {3, 'p'},
        {10, 'q'},
        {1, 'r'},
        {1, 's'},
        {1, 't'},
        {1, 'u'},
        {4, 'v'},
        {4, 'w'},
        {8, 'x'},
        {4, 'y'},
        {10, 'z'}
    };

    int points_player[2];
    points_player[0] = 0;
    points_player[1] = 0;

    char c_invalid[] = {',', '.', '?', '!'};
    for (int player = 0; player < 2; player++)
    {
        for (int i = 0; i < strlen(words[player]); i++)
        {
            char c = tolower(words[player][i]);
            if (strchr(c_invalid, c) == NULL)
            {
                for (int letra = 0; letra < sizeof(points); letra++)
                {
                    if (c == points[letra].letra)
                    {
                        points_player[player] += points[letra].point;
                        break;
                    }
                }
            }
        }
    }

    if (points_player[0] == points_player[1])
    {
        return 0;
    }
    return points_player[0] > points_player[1] ? 1 : 2;
}