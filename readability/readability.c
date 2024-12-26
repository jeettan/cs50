#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int calculateLetter();
int calculateSentence();
int calculateWords();
int calculateScore();

int main(void)
{
    string s = get_string("Text: ");
    int letter = calculateLetter(s);
    int words = calculateWords(s);
    int sentence = calculateSentence(s);
    int score = calculateScore(words, letter, sentence);

    if(score < 1){
        printf("Before Grade 1\n");
    } else if (score >=16) {
        printf("Grade 16+\n");
    } else {
        printf("Grade %i\n", score);
    }

}

int calculateLetter(string s){

    int length = strlen(s);
    int count = 0;

    for(int i = 0; i < length; i++){
        if(isalpha(s[i])) count++;
    }

    printf("Letters: %d \n", count);

    return count;
}

int calculateSentence(string s){

    int length = strlen(s);
    int count = 0;
    char fs = '.';
    char exc = '!';
    char qm = '?';

    for(int i = 0; i < length; i++){
        if(s[i] == fs || s[i] == exc || s[i] == qm) count++;
    }

    printf("Sentences: %d\n", count);

    return count;

}

int calculateWords(string s){

    int length = strlen(s);
    int count = 0;
    char fs = '.';
    char exc = '!';

    for(int i = 0; i < length; i++){
        if(s[i] == ' ') count++;
    }

    //Last value is always a fullstop, so count that as a sentence by adding 1 if the last value of the string is a full stop.

    if(s[length-1] == fs || s[length-1] == exc){
        count++;
    }
    printf("Words: %d\n", count);

    return count;
}

int calculateScore(int words, int letter, int sentence){

    double wordratio = (double)words / 100;

    double L = (double)letter / wordratio;
    double S = (double)sentence / wordratio;
    double index = roundf(0.0588 * L - 0.296 * S - 15.8);

    return index;
}