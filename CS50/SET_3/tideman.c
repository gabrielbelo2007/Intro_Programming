#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
int locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} Pair;

// Array of candidates
char candidates[MAX][10];
Pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
int vote(int rank, char name[], int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, char* argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
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
        strcpy(candidates[i], argv[i + 1]);
    }
    
    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = 0;
        }
    }

    // Clear graph of preferences
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            preferences[i][j] = 0;
        }
    }

    pair_count = 0;
    int voter_count = 0;
    printf("Number of voters: ");
    scanf("%i", &voter_count);

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            char name[10];
            printf("Rank %i: ", j + 1);
            scanf("%s", name);

            if (vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
int vote(int rank, char name[], int ranks[])
{
    int found = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            found = 1;
            break;
        }
    }
    return found ? 0 : 1;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    int scored[candidate_count - 1];
    for (int i = 0; i < candidate_count - 1; i++)
    {
        int candidate = ranks[i]; // 1
        scored[i] = candidate; // 1
        for (int j = 0; j < candidate_count; j++)
        {
            int verificar = 0;
            for (int z = 0; z < candidate_count - 1; z++)
            {
                if (j == scored[z])
                {
                    break;
                }
                verificar++;
            }

            if (verificar == (candidate_count - 1))
            {
                preferences[candidate][j]++;
            }
        }
    }
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0;  j < candidate_count; j++)
        {
            if (i != j)
            {
                if (preferences[i][j] > preferences[j][i])
                {
                    pairs[pair_count].winner = i;
                    pairs[pair_count].loser = j;
                    pair_count++;
                }
            }
        }
    }
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        int candidate_winner = -1;
        int candidate_loser = -1;
        int candidate_position = -1;

        int votes = preferences[pairs[i].winner][pairs[i].loser];
        for (int j = i + 1; j < pair_count; j++)
        {
            if (votes < preferences[pairs[j].winner][pairs[j].loser])
            {
                votes = preferences[pairs[j].winner][pairs[j].loser];

                candidate_winner = pairs[j].winner;
                candidate_loser = pairs[j].loser;
                candidate_position = j;
            }
        }
        if (candidate_winner != -1)
        {
            pairs[candidate_position].winner = pairs[i].winner;
            pairs[candidate_position].loser = pairs[i].loser;

            pairs[i].winner = candidate_winner;
            pairs[i].loser = candidate_loser;
        }
    }
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    int last_arrow_i = 0;
    int last_arrow_j = 0;

    for (int i = 0; i < pair_count; i++)
    {
        locked[pairs[i].winner][pairs[i].loser] = 1;
        locked[pairs[i].loser][pairs[i].winner] = 0;

        last_arrow_i = pairs[i].winner;
        last_arrow_j = pairs[i].loser;
    }

    // Verificando se forma um ciclo, se formar eliminando a ultima seta
    int cycle = 0;
    for (int i = 0; i < pair_count; i++)
    {
        int from = 0;
        int to = 0;
        for (int j = 0; j < pair_count; j++)
        {
            if (i != j)
            {
                if (locked[i][j] == 1)
                {
                    to++;
                }
                if (locked[j][i] == 1)
                {
                    from++;
                }
            }
        }

        if (to == from)
        {
            cycle++;
        }
    }

    if (cycle == candidate_count)
    {
        locked[last_arrow_i][last_arrow_j] = 0;
    }
}

// Print the winner of the election
void print_winner(void)
{
    int strong = 0;
    int greatest = 0;
    for (int i = 0; i < pair_count; i++)
    {
        int from = 0;
        int to = 0;
        for (int j = 0; j < pair_count; j++)
        {
            if (locked[i][j] == 1)
            {
                from++;
            }
            if (locked[j][i] == 1)
            {
                to++;
            }
        }

        if ((from - to) > strong)
        {
            greatest = i;
            strong = from - to;
        }
    }

    printf("%s", candidates[greatest]);
}
