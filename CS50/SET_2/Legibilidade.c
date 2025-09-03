#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int grading(char text[500]);

int main(void)
{
    char text[500];
    printf("Digite seu texto: ");
    fgets(text, sizeof(text), stdin);

    int result = grading(text);
    if (result < 1)
    {
        printf("Before Grade 1");
    }
    else if (result > 16)
    {
        printf("Grade 16+");
    }
    else
    {
        printf("Grade %i", result);
    }
}

int grading(char text[500])
{
    int words = 0;
    int characters = 0;
    int phrases = 0;

    int ignore_space = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (islower(text[i]) != 0 || isupper(text[i]) != 0)
        {
            characters++;
        }
        if (text[i] == ' ' && ignore_space == 0)
        {
            words++;
        }
        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            ignore_space = 1;
            phrases++;
            words++;
        }
        else if (ignore_space == 1)
        {
            ignore_space = 0;
        }
    }

    float L = (characters / (float) words) * 100;
    float S = ((float) phrases / words) * 100;

    float average_grading = 0.0588 * L - 0.296 * S - 15.8;
    return round(average_grading);
}