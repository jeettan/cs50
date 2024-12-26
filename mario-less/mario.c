#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i, j, z;
    char input[200];
    int height = 0;

    //While loop validates input using fgets, then converts it to  %d using sscanf

    while (1)
    {

        printf("Height: ");

        fgets(input, 200, stdin);

        if (input[0] == '\n')
        {
            continue;
        }

        if (sscanf(input, "%d", &height) != 1)
        {
            continue;
        }

        if (height > 0 && height < 9)
        {
            break;
        }

    }

    //If validation is completed, then Mario will be built

    int hash = 1;
    int spaces = height - 1;

    //Hash and spaces determine how many hashes and spaces are there per line

    for (i = 0 ; i < height; i++)

        //Height input determines the y axis of Mario
    {

        //SPACES first initalized depending on the height input, if input is 1, then spaces will = 0 (no spaces)

        for (j = 0; j < spaces; j++)
        {
            printf(" ");
        }
        for (z = 0; z < hash; z++)
        {
            printf("#");
        }
        printf("\n");
        hash = hash + 1;
        spaces = spaces - 1;
    }
}