#include <stdio.h>
#include <stdint.h>
//#define max_width 256


void printing_a_binary(uint8_t value)
{
    int bit = 0;
    printf("Value: \n");
    for(int i=7; i>=0; i--)
    {
        bit = (value >> i) &1;
        printf("%d ", bit);
        
    }
    printf("\n");
};


uint8_t integrating_LSB(uint8_t original, int watermark)
{
    uint8_t mask = 254;

    uint8_t value = original;
    value = mask & value; 
    value = value + watermark; 

    return value;
};

uint8_t integrating_LSB2(uint8_t original, int watermark)
{
    uint8_t mask = 253;

    uint8_t value = original;
    value = mask & value; 
    watermark = watermark << 1;
    value = value + watermark; 

    return value;
};

/*void saving_image(char file_name [], uint8_t array [][max_width], int height, int width )
{
    FILE* f;
    printf("1\n");
    f = fopen(file_name, "w");
    printf("2\n");

    fprintf(f, "{\n");
    printf("3\n");

    for(int i = 0; i < height; i++)
    {
        fprintf(f, "{");
        fprintf(f, "%d", array[i][0]);

        for(int j = 1; j < width; j++)
        {
            fprintf(f, ",");
            fprintf(f, "%d", array[i][j]);

        }
        fprintf(f, "},\n");
    }
    printf("4\n");
    fprintf(f, "}");

    fclose(f);
};*/




