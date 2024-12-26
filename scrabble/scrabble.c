#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
char capitals[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
char lowercase[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

int compute_score(string word);

int main(void)
{


    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    printf("Score 1: %d\n", score1);
    printf("Score 2: %d\n", score2);

    if(score1 > score2){
        printf("Player 1 wins!\n");
    } else if (score2 > score1){
        printf("Player 2 wins!\n");
    } else{
        printf("Tie!\n");
    }
    // TODO: Print the winner
}

int compute_score(string word)
{
    int score = 0;

    int arr_size = sizeof(POINTS)/sizeof(POINTS[0]);


    for (int i = 0; i < strlen(word); i++){

        for(int j =0; j< arr_size; j++){

            if(word[i] == capitals[j]){
                score += POINTS[j];
            } else if(word[i] == lowercase[j]){
                score += POINTS[j];
            }

        }

    }
    return score;

}




