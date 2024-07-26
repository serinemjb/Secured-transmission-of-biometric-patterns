#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include "Finger.h"
#include "ID.h"
#include "functions.h"

int main()
{
    extern uint8_t fingerprint[IMAGE_HEIGHT_fingerprint][IMAGE_WIDTH_fingerprint];
    printf("A\n");
    extern int watermark[IMAGE_HEIGHT_watermark][IMAGE_WIDTH_watermark];
    printf("B\n");
    uint8_t watermarked[IMAGE_HEIGHT_fingerprint][IMAGE_WIDTH_fingerprint];
    printf("C\n");
    for(int i = 0; i<IMAGE_HEIGHT_fingerprint; i++)
    {
        for(int j = 0; j<IMAGE_WIDTH_fingerprint; j++)
        {
            watermarked[i][j] = fingerprint[i][j];

        }
    }
    printf("D\n");

    for(int i = 0; i<IMAGE_HEIGHT_watermark; i++)
    {
        for(int j = 0; j<IMAGE_WIDTH_watermark; j++)
        {
            watermarked[i][j] = integrating_LSB(fingerprint[i][j], watermark[i][j]);

        }
    }
    printf("E\n");

    char file_name[] = "watermarked_LSB.txt";
    printf("F\n");


    FILE* f;
    printf("1\n");
    f = fopen(file_name, "w");
    printf("2\n");

    fprintf(f, "[\n");
    printf("3\n");

    for(int i = 0; i < IMAGE_HEIGHT_fingerprint; i++)
    {
        fprintf(f, "[");
        fprintf(f, "%d", watermarked[i][0]);

        for(int j = 1; j < IMAGE_WIDTH_fingerprint; j++)
        {
            fprintf(f, ",");
            fprintf(f, "%d", watermarked[i][j]);

        }
        fprintf(f, "],\n");
    }
    printf("4\n");
    fprintf(f, "]");

    fclose(f);

    return 0;
}