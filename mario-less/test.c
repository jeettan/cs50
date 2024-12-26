#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char input[1000];
    int num = 0;

    printf("Enter :");

    fgets(input, 1000, stdin);

    if(input[0] == '\n'){
        printf("NULL VALUE");
    }

    if(sscanf(input, "%d", &num) != 1 ){
        printf("Invalid number\n");
    }

    printf("Your num: %d\n", num);

    return 0;

}