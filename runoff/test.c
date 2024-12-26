#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("Enter string: ");

    // ensure string was read
    if (s == NULL)
    {
        return 1;
    }

    string next = get_string("You just entered %s. Enter a new string: ");

    if (next == NULL)
    {
        return 1;
    }

    printf("Your last string was %s\n", s);
}