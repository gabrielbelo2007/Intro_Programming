#include <stdio.h>
#include <string.h>
#include <ctype.h>

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

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
    int points[2];
    points[0] = 0;
    points[1] = 0;

    for (int player = 0; player < 2; player++)
    {
        for (int i = 0; i < strlen(words[player]); i++)
        {
            char c = tolower(words[player][i]);

            switch (c)
            {
            case 'a':
                points[player] += POINTS[0];
                break;
            case 'b':
                points[player] += POINTS[1];
                break;
            case 'c':
                points[player] += POINTS[2];
                break;
            case 'd':
                points[player] += POINTS[3];
                break;
            case 'e':
                points[player] += POINTS[4];
                break;
            case 'f':
                points[player] += POINTS[5];
                break;
            case 'g':
                points[player] += POINTS[6];
                break;
            case 'h':
                points[player] += POINTS[7];
                break;
            case 'i':
                points[player] += POINTS[8];
                break;
            case 'j':
                points[player] += POINTS[9];
                break;
            case 'k':
                points[player] += POINTS[10];
                break;
            case 'l':
                points[player] += POINTS[11];
                break;
            case 'm':
                points[player] += POINTS[12];
                break;
            case 'n':
                points[player] += POINTS[13];
                break;
            case 'o':
                points[player] += POINTS[14];
                break;
            case 'p':
                points[player] += POINTS[15];
                break;
            case 'q':
                points[player] += POINTS[16];
                break;
            case 'r':
                points[player] += POINTS[17];
                break;
            case 's':
                points[player] += POINTS[18];
                break;
            case 't':
                points[player] += POINTS[19];
                break;
            case 'u':
                points[player] += POINTS[20];
                break;
            case 'v':
                points[player] += POINTS[21];
                break;
            case 'w':
                points[player] += POINTS[22];
                break;
            case 'x':
                points[player] += POINTS[23];
                break;
            case 'y':
                points[player] += POINTS[24];
                break;
            case 'z':
                points[player] += POINTS[25];
                break;
            default:
                break;
            }
        }
    }

    if (points[0] == points[1])
    {
        return 0;
    }
    return points[0] > points[1] ? 1 : 2;
}