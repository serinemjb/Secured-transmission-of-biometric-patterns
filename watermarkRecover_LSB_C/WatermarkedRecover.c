#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include "Finger.h"
#include "ID.h"
#include "watermarked_LSB_C1.h"
#include "functions.h"

int main()
{
    extern uint8_t watermarked[IMAGE_HEIGHT_watermarked][IMAGE_WIDTH_watermarked];

    int watermark[IMAGE_HEIGHT_watermarked][IMAGE_WIDTH_watermarked];

    for(int i = 0; i<IMAGE_HEIGHT_watermarked; i++)
    {
        for(int j = 0; j<IMAGE_WIDTH_watermarked; j++)
        {
            watermark[i][j] = watermarked[i][j] & 01;
        }
    }

    char file_name[] = "watermark_LSB_C1.txt";
    printf("F\n");


    FILE* f;
    printf("1\n");
    f = fopen(file_name, "w");
    printf("2\n");

    fprintf(f, "[\n");
    printf("3\n");

    for(int i = 0; i < IMAGE_HEIGHT_watermarked; i++)
    {
        fprintf(f, "[");
        fprintf(f, "%d", watermark[i][0]);

        for(int j = 1; j < IMAGE_WIDTH_watermarked; j++)
        {
            fprintf(f, ",");
            fprintf(f, "%d", watermark[i][j]);

        }
        fprintf(f, "],\n");
    }
    printf("4\n");
    fprintf(f, "]");

    fclose(f);



    return 0;
}