// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 15;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int length = strlen(word);
    char *unit = (char *)malloc((length + 1) * sizeof(char));

    for (int i = 0; i < strlen(word); i++)
    {
        unit[i] = tolower(word[i]);
    }

    unit[length] = '\0';

    for (int i = 0; i < N; i++)
    {
        //  printf("TABLE %i WORD: %s\n", i, table[i]->word);

        if (table[i] == NULL)
        {
            continue;
        }

        if (strcmp(table[i]->word, unit) == 0)
        {
            free(unit);
            return true;
        }
    }
    free(unit);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{

    // TODO: Improve this hash function
    int count = 0;

    unsigned int hash_result = 0;

    hash_result = (word[0] - 'A') % N;

    return hash_result;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    const char *filename = dictionary;

    FILE *file2 = fopen(filename, "r");

    for (int j = 0; j < N; j++)
    {
        table[j] = NULL;
    }

    char c[50];
    char word[LENGTH + 1];

    int i = 0;
    int count = 0;
    int tmp;

    while (fread(&c, sizeof(char), 1, file2))
    {
        if (c[0] == ' ' || c[0] == '\n')
        {
            word[i] = '\0';
            int x = hash(word);

            for (int j = 0; j < N; j++)
            {
                int try = (j + x) % N;
                if (table[try] == NULL)
                {
                    table[try] = malloc(sizeof(node));

                    if (count > 0)
                    {

                        table[tmp]->next = table[try];
                    }

                    strncpy(table[try]->word, word, LENGTH);
                    count++;
                    tmp = try;
                    break;
                }
            }
            i = 0;
        }
        else
        {
            word[i] = c[0];
            i++;
        }
    }

    // Insert last word.
    word[i] = '\0';
    int x = hash(word);

    for (int j = 0; j < N; j++)
    {
        int try = (j + x) % N;
        if (table[try] == NULL)
        {
            table[try] = malloc(sizeof(node));

            if (count > 0)
            {

                table[try]->next = table[tmp];
            }

            strncpy(table[try]->word, word, LENGTH);
            count++;
            tmp = try;
            break;
        }
    }

    fclose(file2);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    int count = 0;

    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            count++;
        }
    }

    return count - 1;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO

    for (int i = 0; i < N; i++)
    {

        free(table[i]);
    }
    return true;
}