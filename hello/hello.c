#include <stdio.h>
#include <stdlib.h>

int main()
{
char name[20];

printf("Please enter your name: ");

scanf("%s", name);

printf("hello, %s\n", name);

return 0;
}