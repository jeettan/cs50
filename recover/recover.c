#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{

    if (argc != 2)
    {
        printf("Please enter in this format: ./recover [IMAGE]\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    typedef uint8_t BYTE;

    BYTE *buffer;

    buffer = malloc(512 * sizeof(uint8_t));

    uint8_t first_value = 255;
    uint8_t second_value = 216;
    uint8_t third_value = 255;
    uint8_t fourth_value = 240;
    uint8_t fifth_value = 224;

    int count = 0;
    int countertwo = 0;
    int jpegfound = 0;
    int arr[50];

    char file[50];

    FILE *img = NULL;

    while (fread(buffer, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {
        countertwo++;

        if (buffer[0] == first_value && buffer[1] == second_value && buffer[2] == third_value && (buffer[3] & fourth_value) == fifth_value)
        {
            arr[count] = countertwo;
            printf("NEW POINT HERE: %d\n", arr[count]);
            count++;

            if (count == 51)
            {
                break;
            }

            if (img == NULL)
            {

                sprintf(file, "%03i.jpg", (count - 1));
                printf("%s\n", file);
                img = fopen(file, "w");
            }
            else
            {

                fclose(img);
                sprintf(file, "%03i.jpg", (count - 1));
                printf("%s\n", file);
                img = fopen(file, "w");
            }
        }

        if (count > 0)
        {
            fwrite(buffer, 512, 1, img);
            printf("Reading at point: %d\n", countertwo);
        }
    }

    fclose(img);
    fclose(input);
    free(buffer);
}
