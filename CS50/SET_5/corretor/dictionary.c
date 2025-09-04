// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
unsigned int word_count = 0;
bool is_loaded = false;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int position = hash(word);
    node *dict_word = table[position];

    while(dict_word != NULL){
        if(strcasecmp(dict_word->word, word) == 0){
            return true;
        }
        dict_word = dict_word->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int sum = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        sum += toupper(word[i]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    for(int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    FILE *file_pointer = fopen(dictionary, "r");
    if(file_pointer == NULL){
        printf("Não foi possível abrir o dicionário.\n");
        return false;
    }

    char word_r[LENGTH + 1];
    while(fscanf(file_pointer, "%s", word_r) != EOF){
        int position = hash(word_r);
        node *n = malloc(sizeof(node));

        if(n == NULL){
            printf("Não foi possível registrar a palavra.\n");
            fclose(file_pointer);
            return false;
        }

        strcpy(n->word, word_r);
        n->next=table[position];

        table[position] = n;
        word_count++;
    }
    fclose(file_pointer);
    is_loaded = true;
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return is_loaded ? word_count : 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for(int i = 0; i < N; i++){
        node *tmp = table[i];

        while(tmp != NULL){
            node *cursor = tmp->next;

            free(tmp);

            tmp = cursor;
        }
        table[i] = NULL;
    }

    return true;
}
