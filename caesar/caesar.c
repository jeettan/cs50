#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int only_digits();

int main(int argc, string argv[])
{
    int argument;
    char capitals[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    char lowercase[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

    if(argc != 2 ){
        printf("Usage: ./caesar key\n");
        exit(1);
    }


        for(int i =0; i< strlen(argv[1]); i++){

        if(isdigit(argv[1][i]) == 0){
            printf("Usage: ./caesar key\n");
            exit(1);
        }
        }

        argument = atoi(argv[1]);

        printf("%d\n",argument);

        string x = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int j =0; j < strlen(x); j++){

        if(islower(x[j]) != 0){

            for(int i=0; i< strlen(lowercase); i++){
            if(lowercase[i] == x[j]){
                printf("%c", lowercase[(i+argument) % 26] );
                }
            }

        } else if(isupper(x[j]) != 0) {

        for(int i=0; i< strlen(capitals); i++){
            if(capitals[i] == x[j]){
                    printf("%c", capitals[(i+argument) % 26] );
                }
            }
        } else{
            printf("%c",x[j]);
        }
    }

    printf("\n");
    }