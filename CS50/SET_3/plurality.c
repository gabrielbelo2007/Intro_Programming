#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    char name[10];
    int votes;
} Candidate;

// Array of candidates
Candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
int vote(char name[]);
void print_winner(void);

int main(int argc, char* argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        strcpy(candidates[i].name, argv[i + 1]);
        candidates[i].votes = 0;
    }

    int voter_count = 0;
    printf("Number of voters: ");
    scanf("%i", &voter_count);
    getchar();

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        char name[10];
        printf("Vote: ");
        scanf("%s", name);
        getchar();

        // Check for invalid vote
        if (vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
int vote(char name[])
{
    int found = 0;
    for (int i  = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            found = 1;
            break;
        }
    }
    return found ? 0 : 1;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int best_points = 0;

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > best_points)
        {
            best_points = candidates[i].votes;
        }
    }

    for (int j = 0; j < candidate_count; j++)
    {
        if (candidates[j].votes == best_points)
        {
            printf("%s\n", candidates[j].name);
        }
    }
}